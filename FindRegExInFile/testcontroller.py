"""File testcontroller.py
Description:
    unittest for controller
Class: TestController
Description:
    tests module controller->browser
"""
from cmdline import GetUserOptions
from controller import show_all
import unittest
import cmdline


# import HTMLTestRunner

class TestController(unittest.TestCase):
    test_framework = {}
    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_controller(self):
        self.test_framework["test"] = True
        self.test_framework["output_format"] = cmdline.OUTPUT_FORMAT_COLOR
        f_list, regexp, o_format = self.cmd_line.get_user_options(self.test_framework)
        assert not show_all(f_list, regexp, o_format), "Module: controller. Function: show_all failed."

    @classmethod
    def tearDownClass(cls):
        print("Test [:controller] Completed Successfully!")


if __name__ == '__main__':
    unittest.main()
