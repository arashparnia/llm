import google.generativeai as palm
import os


class GoogleGenerativeAIWrapper:
    def __init__(self):
        palm.configure(api_key=os.environ['GOOGLE_AI_KEY'])


    def generate_text(self, prompt:str = "The opposite of hot is"):
        response = palm.generate_text(prompt=prompt)
        return response.result  # Outputs: 'cold.'




    def generate_exercise(self, age, difficulty, scenario, character):
        # Generate the prompt for the exercise
        prompt = f"""
            You are a friendly math tutor specializing in teaching young children, 
            specifically {age}-year-olds, the basics of arithmetic in a fun and engaging way. 
            Your goal is to create a simple and enjoyable arithmetic exercise 
            that helps a {age}-year-old understand age-appropriate arithmetic. The exercise should involve arithmetic 
            of two small numbers. for example 'exercise': 'farmer have 2 cows and 2 chickens, how many cows and 
            chickens the farmer has?' 'answer': 4.
            write story followed by an exercise framed in an imaginary setting of {scenario} and the main character
            is {character}. """

        # Generate text using GPT4All
        response = self.generate_text(prompt=prompt)
        return response


