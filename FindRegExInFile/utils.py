"""
    File name: utils.py
    Description: different type of utils can be developed in this file
    Class: LogClass
    Description: implement log functionality

"""

# importing module
import logging


# print user command line parameters to file.log file in current directory:
def init_log():
    # Create and configure logger
    logging.basicConfig(filename="log/file.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    logger = logging.getLogger()

    # Setting the threshold of logger to INFO
    logger.setLevel(logging.INFO)
    return logger


class LogClass:
    pass
