import unittest
import random

from task import slice_ips

class TestCase(unittest.TestCase):
    def test_slice_return_list_type(self):
        ip_address_list = ['127.0.0.1', '192.168.1.1', '8.8.8.8', '192.168.1.101']
        ip_slice = slice_ips(ip_address_list)
        self.assertEqual(type(ip_slice), list)

    def test_not_enough_ips_return_empty_list(self):
        ip_address_list = ['127.0.0.1']
        ip_slice = slice_ips(ip_address_list)
        self.assertEqual(type(ip_slice), list)
        self.assertEqual(len(ip_slice), 0)

    def test_return_ips_list(self):
        ip_address_list = ['127.0.0.1', '192.168.1.1', '8.8.8.8', '192.168.1.101']
        ip_slice = slice_ips(ip_address_list)
        self.assertIn('8.8.8.8', ip_slice)
        self.assertIn('192.168.1.1', ip_slice)

    def test_return_ips_list_random(self):
        ip_address_list = []
        for i in range(5):
            ip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
            ip_address_list.append(ip)
        ip_slice = slice_ips(ip_address_list)
        self.assertEqual(ip_address_list[1], ip_slice[0])
        self.assertEqual(ip_address_list[2], ip_slice[1])