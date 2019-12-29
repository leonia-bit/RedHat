from utils import init_log
import optparse
import re
import os.path


# cmd line: available output format

OUTPUT_FORMAT_COLOR = 0
OUTPUT_FORMAT_UNDERSCORE = 1
OUTPUT_FORMAT_MACHINE = 2


# return output format according to provided parameter
def get_output_format(i):
    switcher = {
        0: 'color',
        1: 'underscore',
        2: 'machine'
    }
    return switcher.get(i, "Invalid output format")


# format and read user input
class GetUserOptions():
    log = None
    parser = None
    usage = None

    # set command line options
    def set_user_options(self):
        self.log = init_log()
        self.log.info('=' * 50)
        self.log.info("Start Program...")

        self.log.info("...")
        self.usage = "usage: %prog [options] arg1 arg2"
        self.parser = optparse.OptionParser(usage=self.usage)
        self.parser = optparse.OptionParser()

        self.parser.add_option("-f", "--files",
                               action="store_true", default=False,
                               help="read data from FILE", metavar="FILE")
        self.parser.add_option("-r", "--regexp",
                               action="store_true", default=False,
                               help="regexp pattern to match in files"
                               )
        self.parser.add_option("-u", "--underscore",
                               action="store_true", default=False,
                               help="print lines with underscore symbol"
                               )
        self.parser.add_option("-c", "--color",
                               action="store_true", default=False,
                               help="print colored lines"
                               )
        self.parser.add_option("-m", "--machine",
                               action="store_true", default=False,
                               help="print machine format lines"
                               )

    # get user options from command line
    def get_user_options(self, test_framework=None):
        files_list = []
        re_pattern = ''
        output_format = ''

        options, args = self.parser.parse_args()
        if test_framework["test"]:
            options.regexp = True
            if test_framework["output_format"] == OUTPUT_FORMAT_COLOR:
                options.color = True
            if test_framework["output_format"] == OUTPUT_FORMAT_UNDERSCORE:
                options.underscore = True
            if test_framework["output_format"] == OUTPUT_FORMAT_MACHINE:
                options.machine = True
            args = ["db/file1.txt", "db/file2.txt", "db/file3.txt", "[q]{4}"]

        self.log.info(("Option: files: y", options.files))
        self.log.info(("Option: regexp: ", options.regexp))
        self.log.info(("Option: color: ", options.color))
        self.log.info(("Option: machine: ", options.machine))
        self.log.info(("Option: underscore: ", options.underscore))

        # check command line: if regexp pattern provided
        if not options.regexp:
            self.log.info("Option: [-r|--regexp] required, please use help. Program terminated!!!")
            exit(0)

        # check command line: if only single option provided for output format c|u|m
        if options.color + options.machine + options.underscore > 1:
            self.log.info("Single options is allowed from: color|machine|underscore. Program terminated!!!")
            exit(0)

        # check command line: if at least one output format option provided
        if not (options.color or options.machine or options.underscore):
            self.log.info("Provide one from following options: color|machine|underscore. Program terminated!!!")
            exit(0)

        # check if provided command line arguments it is real existed file. if not it is regexp
        for arg in args:
            if os.path.exists(arg)  and os.path.isfile(arg):
                files_list.append(arg)
            else:
                re_pattern = arg

        if options.color:
            output_format = get_output_format(OUTPUT_FORMAT_COLOR)
        elif options.machine:
            output_format = get_output_format(OUTPUT_FORMAT_MACHINE)
        else:
            output_format = get_output_format(OUTPUT_FORMAT_UNDERSCORE)

        self.log.info("Output format is: " + output_format)

        return files_list, re_pattern, output_format
