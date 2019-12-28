from cmdline import GetUserOptions
from model import FilesData
import unittest


# import HTMLTestRunner

class TestCommandLine(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cmd_line = GetUserOptions()
        cls.cmd_line.set_user_options()

    def test_model(self):
        f_list, regexp, o_format = self.cmd_line.get_user_options(True)
        file_data_list = FilesData(f_list).get_all()
        assert file_data_list != [], "Module: Model. Function get_all. Files data not available."

    @classmethod
    def tearDownClass(cls):
        print("Test [:model] Completed Successfully!")


if __name__ == '__main__':
    unittest.main()

