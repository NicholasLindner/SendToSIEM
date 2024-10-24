import unittest
from send_data_to_siem_system import Splunk


class TestSplunkDataSender(unittest.TestCase):
    """Unit tests for the Splunk class. Verifies header and paylaad build."""

    # Testing constants
    URL = "https://TestSplunkDataSender.com"
    TOKEN = "token"
    DATA = {"key": "value"}

    def setUp(self):
        """Creates a instance of the Splunk class for testing."""
        self.sender = Splunk(self.URL, self.TOKEN)

    def test_build_headers(self):
        """Tests to see if the correct headers are returned."""
        splunk_test_headers = {
            "Authorization": "Splunk token",
            "Content-Type": "application/json"
        }
        self.assertEqual(self.sender.build_headers(), splunk_test_headers)

    def test_build_payload(self):
        """Tests to see that the build_payload method wraps data in an event structure correctly."""

        splunk_test_payload = {"event": self.DATA}
        self.assertEqual(self.sender.build_payload(self.DATA), splunk_test_payload)


if __name__ == "__main__":
    unittest.main()
