import unittest

from task import read_file_first_line

class TestCase(unittest.TestCase):
    def test_read_file_first_line_return_str_type(self):
        first_line = read_file_first_line("apache_log.txt")
        self.assertEqual(type(first_line), str)

    def test_read_file_first_line_return_str_type(self):
        first_line = read_file_first_line("apache_log.txt")
        self.assertIn('AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"', first_line)