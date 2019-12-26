"""
    File name: formatprint.py
    Description: present template design pattern:
                 defines a basic algorithm in a base class using abstract operation where subclasses override the
                 concrete behavior
    Class: FormatPrint:
    Description: implement template design pattern
                 This code creates a template to prepare formatted string .
                 Here, each parameter represents the attribute to create a part of formatted string like color,
                 underscore and machine format.
"""
from termcolor import colored
import re

FIRST_POSITION = 0
LAST_POSITION = 1


# template class implement abstracts for derived classes to prepare and print different formats
class FormatPrint:

    def __init__(self, file_name, line_number, line, regexp_pattern):
        self.file_name = file_name
        self.line_number = line_number
        self.line = line
        self.regexp_pattern = regexp_pattern

    def prepare_format(self): pass

    def print_format(self): pass

    def go(self):
        self.prepare_format()
        self.print_format()


# derived class from FormatPrint. Implements format and print data with ^ sign under matched patterns
class PrintUnderscore(FormatPrint):
    underscore_line = ''

    def __init__(self, file_name, line_number, line, regexp_pattern):
        FormatPrint.__init__(self, file_name, line_number, line, regexp_pattern)

    # format data: print ^ sign under matched pattern
    def prepare_format(self):

        last_pos = 0
        curr_pos = 0
        line_len = len(self.line)

        while last_pos < line_len:
            curr_pos = last_pos
            search_res = re.search(self.regexp_pattern, self.line[last_pos:line_len])

            if search_res is not None:
                pos = search_res.span()

                while last_pos < pos[FIRST_POSITION] + curr_pos:
                    self.underscore_line += ' '
                    last_pos += 1

                while last_pos < pos[LAST_POSITION] + curr_pos:
                    self.underscore_line += '^'
                    last_pos += 1
            else:
                break

        while last_pos < line_len:
            self.underscore_line += ' '
            last_pos += 1

    # print string: print data and ^ sign under the matched pattern
    def print_format(self):
        print(self.file_name + ": " + self.line_number + ": " + self.line)
        line_len = len(self.file_name) + len(": ") + len(self.line_number) + len(": ")
        print(' ' * line_len + self.underscore_line)
        self.underscore_line = ''


# derived class from FormatPrint. Implements prepare format and print data with color regexp patterns
class PrintColor(FormatPrint):
    color_line = ''

    def __init__(self, file_name, line_number, line, regexp_pattern):
        FormatPrint.__init__(self, file_name, line_number, line, regexp_pattern)

    # prepare Format: insert colored regexp pattern instead of black one
    def prepare_format(self):
        last_pos = 0
        curr_pos = 0
        line_len = len(self.line)

        while last_pos < line_len:
            curr_pos = last_pos
            search_res = re.search(self.regexp_pattern, self.line[last_pos:line_len])

            if search_res is not None:
                pos = search_res.span()

                while last_pos < pos[FIRST_POSITION] + curr_pos:
                    self.color_line += self.line[last_pos]
                    last_pos += 1

                self.color_line += colored(search_res.group(), "yellow")
                last_pos += (pos[LAST_POSITION] - pos[FIRST_POSITION])
            else:
                # end line
                break

        # complete fill data after last pattern
        while last_pos < line_len:
            self.color_line += self.line[last_pos]
            last_pos += 1

    # print data with colored regexp patterns
    def print_format(self):
        print(self.file_name + ":" + self.line_number + ":" + self.color_line)
        self.color_line = ''


# derived class from FormatPrint. Implements print data with machine format
class PrintMachine(FormatPrint):
    matched_data_list = []

    def __init__(self, file_name, line_number, line, regexp_pattern):
        FormatPrint.__init__(self, file_name, line_number, line, regexp_pattern)

    # prepare machine format: file_name:no_line:start_pos:matched_text
    def prepare_format(self):
        curr_pos = 0
        line_len = len(self.line)
        line_data = {}

        while curr_pos < line_len:
            search_res = re.search(self.regexp_pattern, self.line[curr_pos:line_len])

            if search_res is not None:
                pos = search_res.span()

                line_data["file"] = self.file_name
                line_data["line_number"] = self.line_number
                line_data["start_pos"] = pos[FIRST_POSITION] + curr_pos
                line_data["matched_text"] = self.line[pos[FIRST_POSITION]
                                                      + curr_pos:pos[LAST_POSITION] + curr_pos]

                self.matched_data_list.append(line_data.copy())
                curr_pos += pos[LAST_POSITION]
                line_data.clear()
            else:
                # end line
                break

    # print data in machine format: file_name:no_line:start_pos:matched_text
    def print_format(self):
        # format: file_name:no_line:start_pos:matched_text
        for item in self.matched_data_list:
            print(item["file"] + ":" + item["line_number"] + ":" + str(item["start_pos"]) + ":" + item["matched_text"])

        self.matched_data_list.clear()
