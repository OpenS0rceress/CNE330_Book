import unittest

from task import get_first_octet, get_third_octet

class TestCase(unittest.TestCase):
    def test_get_first_octet_return_type(self):
        first_octet = get_first_octet('127.0.0.1')
        first_octet_int = int(first_octet)
        self.assertEqual(type(first_octet_int), int)

    def test_get_third_octet_return_type(self):
        third_octet = get_third_octet('127.127.127.127')
        third_octet_int = int(third_octet)
        self.assertEqual(type(third_octet_int), int)

    def test_get_first_octet_localhost(self):
        self.assertEqual(int(get_first_octet('127.0.0.1')), 127)

    def test_get_first_octet_class_c(self):
        self.assertEqual(int(get_first_octet('192.168.76.1')), 192)

    def test_get_first_octet_two_digit(self):
        self.assertEqual(int(get_first_octet('77.127.76.1')), 77)

    def test_get_third_octet_localhost(self):
        self.assertEqual(int(get_third_octet('127.0.0.1')), 0)

    def test_get_third_octet_class_c(self):
        self.assertEqual(int(get_third_octet('192.168.176.1')), 176)

    def test_get_third_octet_two_digit(self):
        self.assertEqual(int(get_third_octet('77.127.76.1')), 76)