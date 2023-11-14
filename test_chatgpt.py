import unittest
from unittest.mock import patch, Mock
from service.ChatGPTService import ChatGPTService

class TestChatGPTService(unittest.TestCase):

    def setUp(self):
        self.chatgpt = ChatGPTService()

    @patch('requests.post')
    def test_create_thread_and_run_success(self, mock_post):
        # Mock the API response for successful thread creation and run
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = {"thread_id": "test_thread_id", "id": "test_run_id"}

        thread_id, run_id = self.chatgpt.create_thread_and_run([{"text": "Hello, world!"}])
        self.assertEqual(thread_id, "test_thread_id")
        self.assertEqual(run_id, "test_run_id")

    @patch('requests.get')
    def test_check_run_status_success(self, mock_get):
        # Mock the API response for successful run status check
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = {"status": "completed"}

        status = self.chatgpt.check_run_status("test_run_id", "test_thread_id")
        self.assertEqual(status, "completed")

    @patch('requests.get')
    def test_fetch_latest_message_for_thread_success(self, mock_get):
        # Mock the API response for fetching the latest message
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = {
            "data": [{"created_at": "2023-01-01T00:00:00Z", "content": [{"text": {"value": "Test Message"}}]}]
        }

        message = self.chatgpt.fetch_latest_message_for_thread("test_thread_id")
        self.assertEqual(message, "Test Message")

    @patch('requests.post')
    def test_execute_run_success(self, mock_post):
        # Mock the API response for successful run execution
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = {"id": "test_run_id"}

        run_id = self.chatgpt.execute_run("test_thread_id")
        self.assertEqual(run_id, "test_run_id")

    @patch('requests.post')
    def test_create_thread_success(self, mock_post):
        # Mock the API response for successful thread creation
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = {"id": "test_thread_id"}

        thread_id = self.chatgpt.create_thread([{"text": "Hello, world!"}])
        self.assertEqual(thread_id, "test_thread_id")

    @patch('requests.post')
    def test_generate_speech_from_text_success(self, mock_post):
        # Mock the API response for successful speech generation
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.content = b"audio_data"

        audio_data = self.chatgpt.generate_speech_from_text("Hello, world!")
        self.assertEqual(audio_data, b"audio_data")

    @patch('requests.post')
    def test_generate_images_success(self, mock_post):
        # Mock the API response for successful image generation
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = {"data": [{"url": "http://example.com/test_image.jpg"}]}

        image_urls = self.chatgpt.generate_images("A happy dog")
        self.assertEqual(image_urls, ["http://example.com/test_image.jpg"])

if __name__ == '__main__':
    unittest.main()
