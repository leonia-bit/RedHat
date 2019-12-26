"""File name: controller.py
    Description: present Model View Controller Pattern: controller part
                 Controller interacts with <model> MVC.model through the get_all() method which fetches all the records
                  from the server and displayed to the end user.
    Module functions:
    Description: this code represents the controller’s logic. Interacts with MVC.model to fetch data from server (db)
                 and provide it to MVC.view module (client) to view data to end user.
"""

from FindRegExInFile.model import FilesData
from FindRegExInFile import view


# read data entered by user from command line
def get_user_data(file_data_list, line_num):
    file_data = {}
    tmp_list = []
    user_line = ''

    # instead of file name
    file_data["name"] = "user input"
    view.user_input_line_view()
    user_line = input()
    tmp_list.append((line_num, user_line))

    file_data["line"] = tmp_list.copy();
    file_data_list.append(file_data.copy())
    tmp_list.clear()
    file_data.clear()

    # return all data for single line
    return file_data_list


# read data from server (db) using model module and pass it to view model
def show_all(file_list, regexp_pattern, output_format):
    # gets list of all files data
    line_num = 1
    user_input = ''
    file_data_list = FilesData(file_list).get_all()

    # check if user provide files in command line, if not get it online
    if not bool(file_data_list):
        view.user_input_view(regexp_pattern)
        user_input = input()
        while user_input == 'y':
            file_data_list = get_user_data(file_data_list, line_num)
            line_num += 1
            view.user_continue_view()
            user_input = input()

    # check if user provide files list in command line or online
    if not bool(file_data_list):
        return view.end_view()
    # calls view
    return view.show_all_view(file_data_list, regexp_pattern, output_format)


# start program
def start(file_list, regexp_pattern, output_format):
    view.start_view()
    user_input = input()
    if user_input == 'y':
        return show_all(file_list, regexp_pattern, output_format)
    else:
        return view.end_view()
