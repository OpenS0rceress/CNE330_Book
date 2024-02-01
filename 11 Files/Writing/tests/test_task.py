import unittest

from task import write_line_to_file

class TestCase(unittest.TestCase):
    def read_file_first_line(self):
        write_line_to_file("output.txt")
        f = open("output.txt", "r")
        print(f.readlines())
        self.assertFalse(True)