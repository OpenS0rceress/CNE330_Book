import unittest
import random

from task import return_all_192_168

class TestCase(unittest.TestCase):
    def test_slice_return_list_type(self):
        ip_address_list = ['127.0.0.1', '192.168.1.1', '8.8.8.8', '192.168.1.101']
        local_ips = return_all_192_168(ip_address_list)
        self.assertEqual(type(local_ips), list)

    def test_no_ips_return_empty_list(self):
        ip_address_list = ['127.0.0.1']
        local_ips = return_all_192_168(ip_address_list)
        self.assertEqual(len(local_ips), 0)

    def test_return_ips_list(self):
        ip_address_list = ['127.0.0.1', '192.168.1.1', '8.8.8.8', '192.168.1.101']
        ip_slice = return_all_192_168(ip_address_list)
        self.assertIn('192.168.1.1', ip_slice)
        self.assertIn('192.168.1.101', ip_slice)

    def test_return_ips_list_random(self):
        ip_address_list = []
        local_ips_master = []
        for i in range(20):
            if random.randint(0,50) > 40:
                ip = '192.168.' + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                local_ips_master.append(ip)
            else:
                ip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
            ip_address_list.append(ip)
        local_ips = return_all_192_168(ip_address_list)
        for ip_address in local_ips_master:
            self.assertIn(ip_address, local_ips)