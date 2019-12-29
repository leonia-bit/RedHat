"""File testcmdline.py
Description:
    unittest for command line
Class: TestCmdLine
Description:
    tests reading user parameters from command line
"""
from cmdline import GetUserOptions
import unittest
import cmdline


# import HTMLTestRunner

class TestCmdLine(unittest.TestCase):
    test_framework = {}

    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_cmd_line(self):
        self.test_framework["test"] = True
        self.test_framework["output_format"] = cmdline.OUTPUT_FORMAT_COLOR
        f_list, regexp, o_format = self.cmd_line.get_user_options(self.test_framework)
        assert o_format != '', "Module: cmdline. Output format can't be empty."
        assert regexp != '', "Module: cmdline: Regexp pattern can't be empty"
        assert f_list != [], "Module: cmdline: File list can't be empty"

    @classmethod
    def tearDownClass(cls):
        print("Test [:cmdline] Completed Successfully!")


if __name__ == '__main__':
    unittest.main()

    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../results"))
