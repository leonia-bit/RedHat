from cmdline import GetUserOptions
import controller

if __name__ == '__main__':
    test_framework = {}
    cmd_line = GetUserOptions()
    test_framework["test"] = False

    # init command line input format
    cmd_line.set_user_options()

    file_list, regexp_pattern, output_format = cmd_line.get_user_options(test_framework)
    controller.start(file_list, regexp_pattern, output_format)
