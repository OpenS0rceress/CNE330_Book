import unittest

from task import dns_resolve


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_dns_resolve_return_str_type(self):
        ip_result = dns_resolve('Windows')
        self.assertEqual(type(ip_result), str)

    def test_dns_resolve_linux(self):
        ip_result = dns_resolve('Linux')
        self.assertEqual('192.168.1.101', ip_result)

    def test_dns_resolve_gateway(self):
        ip_result = dns_resolve('Gateway')
        self.assertEqual('192.168.1.1', ip_result)

    def test_dns_resolve_windows(self):
        ip_result = dns_resolve('Windows')
        self.assertEqual('192.168.1.102', ip_result)

    def test_create_network_dns_none_type(self):
        ip_result = dns_resolve('NotOnTheNetwork')
        self.assertEqual(None, ip_result)