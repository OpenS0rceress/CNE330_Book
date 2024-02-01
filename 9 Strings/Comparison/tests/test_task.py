import unittest

from task import check_in, check_not_in

class TestCase(unittest.TestCase):
    def test_check_in_type(self):
        check_result = check_in('127.0.0.1', "127")
        self.assertEqual(type(check_result), bool)

    def test_check_not_in_type(self):
        check_result = check_in('127.0.0.1', "127")
        self.assertEqual(type(check_result), bool)

    def test_check_in_insidee(self):
        check_result = check_in('127.0.0.1', "127")
        self.assertEqual(check_result, True)

    def test_check_in_type_not_inside(self):
        check_result = check_in('127.0.0.1', "192")
        self.assertEqual(check_result, False)

    def test_check_not_in_not_inside(self):
        check_result = check_not_in('127.0.0.1', "192")
        self.assertEqual(check_result, True)

    def test_check_not_in_inside(self):
        check_result = check_not_in('127.0.0.1', "127")
        self.assertEqual(check_result, False)