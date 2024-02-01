import unittest

from task import create_clone

class TestCase(unittest.TestCase):
    def test_slice_return_list_type(self):
        ip_address_list = ['127.0.0.1', '192.168.1.1', '8.8.8.8', '192.168.1.101']
        ip_list_copy = create_clone(ip_address_list)
        self.assertEqual(type(ip_list_copy), list)

    def test_return_ips_list(self):
        ip_address_list = ['127.0.0.1', '192.168.1.1', '8.8.8.8', '192.168.1.101']
        ip_list_copy = create_clone(ip_address_list)
        ip_list_copy.append("127.0.0.2")
        self.assertNotEqual(ip_address_list, ip_list_copy)
        for ip_address in ip_address_list:
            self.assertIn(ip_address, ip_list_copy)