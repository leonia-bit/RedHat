from cmdline import GetUserOptions
import controller

if __name__ == '__main__':
    cmd_line = GetUserOptions()

    # init command line input format
    cmd_line.set_user_options()

    file_list, regexp_pattern, output_format = cmd_line.get_user_options()
    controller.start(file_list, regexp_pattern, output_format)
