"""File testmodel.py
Description:
    unittest for model unit
Class: TestModel
Description:
    tests module model->db
"""
from cmdline import GetUserOptions
from model import FilesData
import cmdline
import unittest


# import HTMLTestRunner

class TestModel(unittest.TestCase):
    test_framework = {}
    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_model(self):
        self.test_framework["test"] = True
        self.test_framework["output_format"] = cmdline.OUTPUT_FORMAT_COLOR
        f_list, regexp, o_format = self.cmd_line.get_user_options(self.test_framework)
        file_data_list = FilesData(f_list).get_all()
        assert file_data_list != [], "Module: Model. Function get_all. Files data not available."

    @classmethod
    def tearDownClass(cls):
        print("Test [:model] Completed Successfully!")


if __name__ == '__main__':
    unittest.main()

