import unittest
from unittest.mock import MagicMock
from mathtutor import MathTutor
from ChatGPT import ChatGPT


class TestMathTutor(unittest.TestCase):

    def setUp(self):
        self.chatgpt = ChatGPT()
        self.tutor = MathTutor(self.chatgpt)

    def test_extract_number(self):
        result = MathTutor.extract_number("The result is 8.")
        self.assertEqual(result, "8")

    def test_generate_problem(self):
        self.chatgpt.query = MagicMock(return_value="Solve: 5 + 3")
        problem = self.tutor.generate_problem()
        self.assertEqual(problem, "Solve: 5 + 3")

    def test_extract_number(self):
        result = self.tutor.extract_number("The result is 8.")
        self.assertEqual(result, "8")

    def test_get_solution(self):
        self.chatgpt.query = MagicMock(return_value="The result is 8.")
        solution = self.tutor.get_solution("Solve: 5 + 3")
        self.assertEqual(solution, "8")

    def test_adjust_difficulty(self):
        self.chatgpt.query = MagicMock(return_value="Difficulty should be 2.")
        self.tutor.adjust_difficulty(True, 5)
        self.assertEqual(self.tutor.difficulty, 2)

    def test_evaluate_performance(self):
        self.tutor.start_timer()
        self.tutor.stop_timer()  # Assume zero time elapsed for simplicity
        correctness, time_taken = self.tutor.evaluate_performance("8", "8")
        self.assertTrue(correctness)
        self.assertAlmostEqual(time_taken, 0.0,
                               places=5)  # Assert that time_taken is almost equal to 0.0 with up to 1e-5 seconds of difference


if __name__ == '__main__':
    unittest.main()
