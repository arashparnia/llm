import time
import re  # Import the regex module


class MathTutor:
    def __init__(self, chatgpt):
        self.chatgpt = chatgpt
        self.difficulty = 1
        self.age = 4
        self.start_time = None
        self.end_time = None

    def generate_problem(self):
        prompt = f"""
        you will generate a text problem should have enough details and context for dall-e 3 model to 
        generate an accurate image for it. 
        You are a friendly math tutor specializing in teaching young children, 
        specifically {self.age}-year-olds, the basics of arithmetic in a fun and engaging way. 
        Your goal is to create a simple and enjoyable arithmetic exercise 
        that helps a {self.age}-year-old understand age appropriate arithmetic. 
        The exercise should involve arithmetic of two small numbers, 
        and it should be framed in a playful scenario that would appeal to a young child's imagination.
        The problem will vary in difficulty but even the highest difficulty should be appropriate for a small child.
        please set the difficulty to {self.difficulty}. only reply with the problem itself and nothing else . 
        
        """
        problem = self.chatgpt.query(prompt)
        return problem

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    @staticmethod
    def extract_number(text):
        """Extracts the first number found in the text."""
        match = re.search(r'\b\d+\b', text)
        if match:
            return match.group()
        else:
            raise ValueError("No number found in text")

    def extract_difficulty(self, text):
        """Extracts the first number found in the text."""
        match = re.search(r'\b\d+\b', text)
        if match:
            return int(match.group())
        else:
            raise ValueError("No difficulty level found in text")

    def evaluate_performance(self, user_answer, correct_answer):
        correctness = user_answer == correct_answer
        time_taken = self.end_time - self.start_time
        return correctness, time_taken

    def adjust_difficulty(self, correctness, time_taken):
        prompt = f"""
        Adjust difficulty based on correctness: {correctness} and time taken: {time_taken}. 
        Current difficulty: {self.difficulty}.
        If the time is less than one minute that means we can move on to a higher difficulty {self.difficulty+1}.
        if the time is really long even if the answer is correct we should stay with current difficulty.
        if the time is really long and the answer is wrong then we should go back one level of difficulty.
        """
        response_text = self.chatgpt.query(prompt)
        try:
            self.difficulty = self.extract_difficulty(response_text)
        except ValueError as e:
            print(f"Error: {e}")

    def get_solution(self, problem):
        prompt = f"return only the  the numerical solution for the problem as a number on its own with no text: {problem} "
        solution_text = self.chatgpt.query(prompt)
        try:
            solution = self.extract_number(solution_text)
            return solution
        except ValueError as e:
            print(f"Error: {e}")
