import unittest

from task import linux_mac_windows

class TestCase(unittest.TestCase):
    def test_none(self):
        print("Testing 1 and 15")
        self.assertEqual(linux_mac_windows(1, 16), [5, 3, 1])

    def test_one_linux(self):
        print("Testing 1 and 15")
        self.assertEqual(linux_mac_windows(1, 16), [5, 3, 1])

    def test_one_mac(self):
        print("Testing 1 and 15")
        self.assertEqual(linux_mac_windows(1, 16), [5, 3, 1])

    def test_one_windows(self):
        print("Testing 1 and 15")
        self.assertEqual(linux_mac_windows(1, 16), [5, 3, 1])

    def test_ip_range_1_15(self):
        print("Testing 1 and 15")
        self.assertEqual(linux_mac_windows(1, 16), [5, 3, 1])


    def test_ip_range_1_60(self):
        print("Testing 1 and 60")
        self.assertEqual(linux_mac_windows(1, 60), [19, 11, 3])


    def test_ip_range_100_200(self):
        print("Testing 1 and 500")
        self.assertEqual(linux_mac_windows(1, 500), [166, 99, 33])


    def test_ip_range_1_255(self):
        print("Testing 1700 and 30000")
        self.assertEqual(linux_mac_windows(1700, 30000), [9433, 5660, 1886])