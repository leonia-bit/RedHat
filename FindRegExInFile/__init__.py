#!/usr/bin/python
from FindRegExInFile.utils import LogClass
from FindRegExInFile.utils import init_log
from FindRegExInFile.model import FilesData
import optparse
import re
import controller


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


# get user options from command line
def get_user_options():
    files_list = []
    re_pattern = ''

    log = init_log()
    log.info('=' * 50)
    log.info("Start Program...")

    log.info("...")

    usage = "usage: %prog [options] arg1 arg2"
    parser = optparse.OptionParser(usage=usage)

    parser = optparse.OptionParser()

    parser.add_option("-f", "--files",
                      action="store_true", default=False,
                      help="read data from FILE", metavar="FILE")
    parser.add_option("-r", "--regexp",
                      action="store_true", default=False,
                      help="regexp pattern to match in files"
                      )
    parser.add_option("-u", "--underscore",
                      action="store_true", default=False,
                      help="print lines with underscore symbol"
                      )
    parser.add_option("-c", "--color",
                      action="store_true", default=False,
                      help="print colored lines"
                      )
    parser.add_option("-m", "--machine",
                      action="store_true", default=False,
                      help="print machine format lines"
                      )

    options, args = parser.parse_args()

    log.info(("Option: files: y", options.files))
    log.info(("Option: regexp: ", options.regexp))
    log.info(("Option: color: ", options.color))
    log.info(("Option: machine: ", options.machine))
    log.info(("Option: underscore: ", options.underscore))

    # check command line: if regexp pattern provided
    if not options.regexp:
        log.info("Option: [-r|--regexp] required, please use help. Program terminated!!!")
        exit(0)

    # check command line: if only single option provided for output format c|u|m
    if options.color + options.machine + options.underscore > 1:
        log.info("Single options is allowed from: color|machine|underscore. Program terminated!!!")
        exit(0)

    # check command line: if at least one output format option provided
    if options.color + options.machine + options.underscore == 0:
        log.info("Provide one from following options: color|machine|underscore. Program terminated!!!")
        exit(0)
    '''
    Get command line arguments files and regexp pattern. 
    Limitation: file extension should be start from file.*
    Regexp pattern can't be start from keyword: file
    '''
    for arg in args:
        if re.search("^file.*", arg):
            files_list.append(arg)
        else:
            re_pattern = arg

    # set output format option
    output_format = ''
    if options.color:
        output_format = get_output_format(OUTPUT_FORMAT_COLOR)
    elif options.machine:
        output_format = get_output_format(OUTPUT_FORMAT_MACHINE)
    else:
        output_format = get_output_format(OUTPUT_FORMAT_UNDERSCORE)

    log.info("Output format is: " + output_format)

    return files_list, re_pattern, output_format


if __name__ == '__main__':
    file_list, regexp_pattern, output_format = get_user_options()
    controller.start(file_list, regexp_pattern, output_format)
