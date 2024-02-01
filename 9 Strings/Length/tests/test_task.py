import unittest

from task import compare_ip_length

class TestCase(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(compare_ip_length('127.0.0.1', '127.0.0.1')), str, msg="Testing 127.0.0.1 and 127.0.0.1")

    def test_longer_ip_b(self):
        self.assertEqual(compare_ip_length('127.0.0.1', '127.0.0.10'), '127.0.0.10', msg="Testing 127.0.0.1 and 127.0.0.10")

    def test_same_ip(self):
        self.assertEqual(compare_ip_length('127.0.0.1', '127.0.0.1'), '127.0.0.1', msg="Testing 127.0.0.1 and 127.0.0.1")

    def test_longer_ip_a(self):
        self.assertEqual(compare_ip_length('127.0.0.101', '127.0.0.1'), '127.0.0.101', msg="Testing 127.0.0.101 and 127.0.0.1")