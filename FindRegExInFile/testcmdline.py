from cmdline import GetUserOptions
import unittest


# import HTMLTestRunner

class TestCommandLine(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_cmdline(self):
        f_list, regexp, o_format = self.cmd_line.get_user_options(True)
        assert o_format != '', "Module: cmdline. Output format can't be empty."
        assert regexp != '', "Module: cmdline: Regexp pattern can't be empty"
        assert f_list != [] , "Module: cmdline: File list can't be empty"

    @classmethod
    def tearDownClass(cls):
        print("Test [:cmdline] Completed Successfully!")


if __name__ == '__main__':
    unittest.main()

    # ToDo: add 5. HTML report after: 1. unittest will cover, 2. STP, 3. ReleaseNotes
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
    # output='C:/Users/mkbc3/PycharmProjects/RedHat/FindRegExInFile/results'))
