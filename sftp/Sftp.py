#!/usr/bin/env python

import logging


class Sftp:

    logger = logging.getLogger()

    def __init__(self):
        self.logger.setLevel(logging.INFO)

    def do_something(self):
        self.logger.info('info something')
        self.logger.debug('debug something')
        self.logger.error('error something')
        self.logger.critical('critical something')
