"""File name: view.py
    Description: present Model View Controller Pattern: view part
                 View represents the client, which interact with the end user.
    Module functions:
    Description: this code represents the model’s data to user.
"""
from FindRegExInFile.formatprint import *
import re

# tuple holders defines
LINE_NUMBER_PLACE = 0
LINE_PLACE = 1


# interface to continue or not enter lines from cmd line
def user_continue_view():
    print("Would you like to continue?")


# interface to enter new line from cmd line
def user_input_line_view():
    print("Enter line: ")


# interface to start enter lines to inspect from cmd line
def user_input_view(regexp_pattern):
    print("Files to inspect were not provided regexp pattern is: " + regexp_pattern)
    print('Do you want enter lines to inspect? [y/n]')


# interface to view all matched data according to regexp pattern and output format
def show_all_view(file_data_list, regexp_pattern, output_format):
    print('In our db we have %i lines. Here they are:' % len(file_data_list))
    print("Lines that matched following pattern: " + regexp_pattern + " will be displayed")
    print("Following format was selected by user: " + output_format)

    for data in file_data_list:
        for line in data["line"]:
            if re.search(regexp_pattern, line[LINE_PLACE]):
                if output_format == 'color':
                    print_color = PrintColor(data["name"], str(line[LINE_NUMBER_PLACE]),
                                             line[LINE_PLACE], regexp_pattern)
                    print_color.go()
                elif output_format == 'underscore':
                    print_underscore = PrintUnderscore(data["name"], str(line[LINE_NUMBER_PLACE]),
                                                       line[LINE_PLACE], regexp_pattern)
                    print_underscore.go()
                elif output_format == 'machine':
                    print_machine = PrintMachine(data["name"], str(line[LINE_NUMBER_PLACE]),
                                                 line[LINE_PLACE], regexp_pattern)
                    print_machine.go()


# interface to stat interact with user
def start_view():
    print('RedHat - coding task')
    print('Do you want to see file data?[y/n]')


# interface to finish iteract with user
def end_view():
    print('Goodbye!')
