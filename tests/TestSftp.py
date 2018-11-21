#!/usr/bin/env python

import unittest
import logging
import requests


class TestSftp(unittest.TestCase):

    logger = logging.getLogger()

    def __init__(self):
        self.logger.setLevel(logging.INFO)

    def setUp(self):
        pass

    def test_typical(self):
        request = requests.get('https://api.github.com/events')
        self.assertIsNotNone(request)
        print(request.text)

if __name__ == '__main__':
    unittest.main()
