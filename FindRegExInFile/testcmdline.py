from cmdline import GetUserOptions
import unittest


class TestCommandLine(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_cmdline(self):
        f_list, regexp, o_format = self.cmd_line.get_user_options(True)
        assert o_format != '', "Output format can't be empty."
        assert regexp != '', "Regexp pattern can't be empty"

    @classmethod
    def tearDownClass(cls):
        print("Test Completed Successfully!")


if __name__ == '__main__':

    unittest.main()
