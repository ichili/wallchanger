import logging
import sys
import os.path


def setup_custom_logger(name, filename):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


def setup_global_logger():
    logpath = os.path.dirname(sys.argv[0])
    logpath = os.path.join(logpath, 'log.txt')
    logger = setup_custom_logger('glogger', logpath)
    return logger
