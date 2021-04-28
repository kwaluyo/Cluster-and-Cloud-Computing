#!/usr/bin/python3

from subprocess import Popen
from datetime import datetime
import logging
import argparse
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Reconnect to stream when disconnected
while True:
    # Change python to python3 to deploy in Ubuntu
    process = Popen("python " + "stream_tweet.py", shell=True)
    process.wait()
    logger.error('Error occured at ' + str(datetime.now()) + ' and is restarting now.\n')