import unittest

from task import create_ip_address

class TestCase(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(create_ip_address(127, 0, 0, 1)), str)