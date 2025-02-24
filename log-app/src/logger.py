#!/usr/bin/env python

import sys
import logging
import time
import json
from random import randint
from pythonjsonlogger.json import JsonFormatter

import cowsay

class CustomJsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        super(CustomJsonFormatter, self).format(record)
        output = {k: str(v) for k, v in record.__dict__.items()}
        return json.dumps(output)
    
logger = logging.getLogger('')
logger.setLevel(logging.NOTSET)
sh = logging.StreamHandler(sys.stdout)

formatter_stdout = logging.Formatter( \
    '[%(asctime)s] STDOUT %(levelname)s \
    [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', \
    datefmt='%a, %d %b %Y %H:%M:%S')

formatter_stderr = logging.Formatter(\
    '[%(asctime)s] STDERR %(levelname)s \
    [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', \
    datefmt='%a, %d %b %Y %H:%M:%S')

cf = CustomJsonFormatter()
sh.setFormatter(cf)
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)

def cow():
    return cowsay.cow("Moooo...")

def test_logger():
    logger.info("This is a log message", extra={"app_custom_level": "info", "request_id": "12ab34cd56ef" })
    logger.critical("This is a log message", extra={"app_custom_level": "critical", "request_id": "12ab34cd56ef"})
    logger.warning("This is a log message", extra={"app_custom_level": "warning", "request_id": "12ab34cd56ef"})
    logger.error("This is a log message", extra={"app_custom_level": "error", "request_id": "12ab34cd56ef"})
    logger.debug("This is a log message", extra={"app_custom_level": " debug", "request_id": "12ab34cd56ef"})

if __name__ == "__main__":
    cow()
    while True:
        test_logger()
        s = randint(30,120)
        print(f"Sleeping for {s} seconds")
        time.sleep(s)
