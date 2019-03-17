import unittest

class Init(unittest.TestCase):

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')