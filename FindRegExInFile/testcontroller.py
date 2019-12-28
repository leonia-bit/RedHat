from cmdline import GetUserOptions
from controller import show_all
import unittest


# import HTMLTestRunner

class TestCommandLine(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_cmdline(self):
        f_list, regexp, o_format = self.cmd_line.get_user_options(True)
        assert not show_all(f_list, regexp, o_format), "Function: show_all failed."

    @classmethod
    def tearDownClass(cls):
        print("Test [:controller] Completed Successfully!")


if __name__ == '__main__':
    unittest.main()
