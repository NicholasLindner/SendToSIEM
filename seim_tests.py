import unittest
from send_data_to_seim_system import Splunk


class TestSplunkDataSender(unittest.TestCase):

    # Testing constantts
    URL = "https://TestSplunkDataSender.com"
    TOKEN = "token"
    DATA = {"key": "value"}

    def setUp(self):
        self.sender = Splunk(self.URL, self.TOKEN)

    def test_build_headers(self):
        splunk_test_headers = {
            "Authorization": "Splunk token",
            "Content-Type": "application/json"
        }
        self.assertEqual(self.sender.build_headers(), splunk_test_headers)

    def test_build_payload(self):
        splunk_test_payload = {"event": self.DATA}
        self.assertEqual(self.sender.build_payload(self.DATA), splunk_test_payload)


if __name__ == "__main__":
    unittest.main()
