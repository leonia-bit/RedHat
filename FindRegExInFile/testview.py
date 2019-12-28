from cmdline import GetUserOptions
from view import show_all_view
from model import FilesData
import unittest


# import HTMLTestRunner

class TestCommandLine(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_cmdline(self):
        f_list, regexp, o_format = self.cmd_line.get_user_options(True)
        file_data_list = FilesData(f_list).get_all()
        assert not show_all_view(file_data_list, regexp, o_format), "Module: view Function: show_all_view failed."

    @classmethod
    def tearDownClass(cls):
        print("Test [:view] Completed Successfully!")


if __name__ == '__main__':
    unittest.main()
