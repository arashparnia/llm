import unittest
from unittest.mock import MagicMock, patch
from ChatGPT import ChatGPT
import openai

class TestChatGPT(unittest.TestCase):

    def setUp(self):
        self.chatgpt = ChatGPT()

    @patch('openai.ChatCompletion.create')
    def test_query_success(self, mock_create):
        # Mock the API response
        mock_create.return_value = {
            "choices": [{"message": {"content": "The answer is 5."}}]
        }

        # Test a successful query
        response = self.chatgpt.query("What is 2 + 3?")
        self.assertEqual(response, "The answer is 5.")

    @patch('openai.ChatCompletion.create')
    def test_query_failure(self, mock_create):
        # Mock an API error
        mock_create.side_effect = openai.error.OpenAIError("API error")

        # Test a failed query
        with self.assertRaises(Exception) as context:
            self.chatgpt.query("What is 2 + 3?")
        self.assertEqual(str(context.exception), "Failed to query API: API error")

    def test_query_max_tokens(self):
        # This test will actually send a query to the API, which is not ideal.
        # It's here to demonstrate how you might test the max_tokens argument,
        # but in a real test suite, you would probably want to use mocking.
        response = self.chatgpt.query("What is 2 + 3?", max_tokens=10)
        self.assertTrue(isinstance(response, str))

if __name__ == '__main__':
    unittest.main()
