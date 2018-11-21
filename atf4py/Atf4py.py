#!/usr/bin/env python

import unittest
import logging


class Atf4py(unittest.TestCase):

    logger = logging.getLogger()

    def __init__(self):
        self.logger.setLevel(logging.INFO)

    def setUp(self):
        pass
