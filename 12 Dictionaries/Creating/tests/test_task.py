import unittest

from task import create_network_dns


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_create_network_dns_return_dict_type(self):
        ip_dict = create_network_dns()
        self.assertEqual(type(ip_dict), dict)

    def test_create_network_dnse(self):
        ip_dict = create_network_dns()
        self.assertEqual(ip_dict['Linux'], '192.168.1.101')
        self.assertEqual(ip_dict['Gateway'], '192.168.1.1')
        self.assertEqual(ip_dict['Windows'], '192.168.1.102')