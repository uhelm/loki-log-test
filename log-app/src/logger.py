#!/usr/bin/env python

import sys
import logging
import time
from random import randint
from pythonjsonlogger.json import JsonFormatter

import cowsay

logger = logging.getLogger('')
logger.setLevel(logging.NOTSET)
sh = logging.StreamHandler(sys.stdout)
#eh = logging.StreamHandler(sys.stderr)
formatter_stdout = logging.Formatter( \
    '[%(asctime)s] STDOUT %(levelname)s \
    [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', \
    datefmt='%a, %d %b %Y %H:%M:%S')

formatter_stderr = logging.Formatter(\
    '[%(asctime)s] STDERR %(levelname)s \
    [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', \
    datefmt='%a, %d %b %Y %H:%M:%S')
#sh.setFormatter(formatter_stdout)
#eh.setFormatter(formatter_stderr)
sh.setFormatter(JsonFormatter())
sh.setLevel(logging.DEBUG)
#eh.setLevel(logging.WARNING)
logger.addHandler(sh)
#logger.addHandler(eh)
#logger.addHandler(sh)

def cow():
    return cowsay.cow("Moooo...")

def test_logger():
    logger.info("Hello", extra={"level": "info"})
    logger.critical("Hello", extra={"level": "critical"})
    logger.warning("Hello", extra={"level": "warning"})
    logger.error("Hello", extra={"level": "error"})
    logger.debug("Hello", extra={"level": " debug"})

if __name__ == "__main__":
    cow()
    while True:
        test_logger()
        s = randint(1,30)
        print(f"Sleeping for {s} seconds")
        time.sleep(s)
