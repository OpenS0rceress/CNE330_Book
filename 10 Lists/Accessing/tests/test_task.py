import unittest

from task import access_first_element,access_second_element,access_last_element

class TestCase(unittest.TestCase):
    def test_access_first_element_return_type(self):
        access_first = access_first_element(['127.0.0.1','192.168.0.1',
                                                   '10.0.0.1','192.168.1.1'])
        access_first_str = str(access_first)
        self.assertEqual(type(access_first_str), str)

    def test_access_second_element_return_type(self):
        access_second = access_second_element(['127.0.0.1','192.168.0.1',
                                                   '10.0.0.1','192.168.1.1'])
        access_second_str = str(access_second)
        self.assertEqual(type(access_second_str), str)

    def test_access_last_element_return_type(self):
        access_last = access_last_element(['127.0.0.1','192.168.0.1',
                                                   '10.0.0.1','192.168.1.1'])
        access_last_str = str(access_last)
        self.assertEqual(type(access_last_str), str)

    def test_access_first_element_localhost(self):
        self.assertEqual(str(access_first_element(['127.0.0.1', '192.168.0.1',
                                                    '10.0.0.1', '192.168.1.1'])), '127.0.0.1')



    def test_access_second_element_localhost(self):
        self.assertEqual(str(access_second_element(['127.0.0.1', '192.168.0.1',
                                                   '10.0.0.1', '192.168.1.1'])), '192.168.0.1')




    def test_access_last_element_localhost(self):
        self.assertEqual(str(access_last_element(['127.0.0.1', '192.168.0.1',
                                                   '10.0.0.1', '192.168.1.1'])), '192.168.1.1')

