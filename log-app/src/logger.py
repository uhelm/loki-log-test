#!/usr/bin/env python

import sys
import logging
import time
from cowsay import cowsay
from random import randint

logger = logging.getLogger('')
logger.setLevel(logging.NOTSET)
sh = logging.StreamHandler(sys.stdout)
eh = logging.StreamHandler(sys.stderr)
formatter_stdout = logging.Formatter('[%(asctime)s] STDOUT %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
formatter_stderr = logging.Formatter('[%(asctime)s] STDERR %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
sh.setFormatter(formatter_stdout)
eh.setFormatter(formatter_stderr)
sh.setLevel(logging.DEBUG)
eh.setLevel(logging.WARNING)
logger.addHandler(eh)
logger.addHandler(sh)

def cow():
    return cowsay("Moooo...")

def test_logger():
    logger.info("Hello info")
    logger.critical("Hello critical")
    logger.warning("Hello warning")
    logger.error("Hello error")
    logger.debug("Hello debug")

if __name__ == "__main__":
    print(cow())
    while True:
        test_logger()
        s = randint(1,30)
        print(f"Sleeping for {s} seconds")
        time.sleep(s)