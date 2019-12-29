"""File testview.py
Description:
    unittest for view formatted data
Class: TestView
Description:
    tests module view->HTML
"""
from cmdline import GetUserOptions
import cmdline
from view import show_all_view
from model import FilesData
import unittest


# import HTMLTestRunner

class TestView(unittest.TestCase):
    test_framework = {}

    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_view_color(self):
        self.test_framework["test"] = True
        self.test_framework["output_format"] = cmdline.OUTPUT_FORMAT_COLOR
        f_list, regexp, o_format = self.cmd_line.get_user_options(self.test_framework)
        file_data_list = FilesData(f_list).get_all()
        assert not show_all_view(file_data_list, regexp, o_format), "Module: view Function: show_all_view failed."

    def test_view_underscore(self):
        self.test_framework["test"] = True
        self.test_framework["output_format"] = cmdline.OUTPUT_FORMAT_UNDERSCORE
        f_list, regexp, o_format = self.cmd_line.get_user_options(self.test_framework)
        file_data_list = FilesData(f_list).get_all()
        assert not show_all_view(file_data_list, regexp, o_format), "Module: view Function: show_all_view failed."

    def test_view_machine(self):
        self.test_framework["test"] = True
        self.test_framework["output_format"] = cmdline.OUTPUT_FORMAT_MACHINE
        f_list, regexp, o_format = self.cmd_line.get_user_options(self.test_framework)
        file_data_list = FilesData(f_list).get_all()
        assert not show_all_view(file_data_list, regexp, o_format), "Module: view Function: show_all_view failed."

    @classmethod
    def tearDownClass(cls):
        print("Test [:view] Completed Successfully!")


if __name__ == '__main__':
    unittest.main()
