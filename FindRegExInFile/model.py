#!/usr/bin/python
"""File Model.py
Description:
    Implement design pattern logic for: Model View Controller Pattern (MVC)
Class: FilesData
Description:
    It consists of pure application logic, which interacts with the different types of database.
    It includes all the information to represent data to the end user.
"""


class FilesData:
    file_data_list = []
    file_name_list = []

    # class constructor: get list of files to read
    def __init__(self, file_name_list=None):
        self.file_name_list = file_name_list.copy()

    # returns data
    def data(self):
        return self.file_data_list

    # returns all files data
    def get_all(self):
        # temp variables
        file_data = {}
        tmp_list = []
        file_data.setdefault("line", [])

        # run in all files. manage two cases: 1. file is not exists 2. Empty file
        for name in self.file_name_list:
            line_num = 0

            # try block: in case file not exists
            try:
                f = open(name, "r")
            except (FileNotFoundError, IOError):
                print("File: " + name + " not found")
            else:
                file_data["name"] = name
                for line in f:
                    line_num += 1
                    tmp_list.append((line_num, line))

                # Add information to log file that file is empty
                if len(tmp_list) == 0:
                    tmp_list.append((0, "File is empty"))

                file_data["line"] = tmp_list.copy();
                self.file_data_list.append(file_data.copy())

                # clear resources
                tmp_list.clear()
                file_data.clear()
                f.close()
        return self.file_data_list.copy()
