import google.generativeai as palm
import os
import json


class GoogleGenerativeAIWrapper:
    def __init__(self):
        palm.configure(api_key=os.environ['GOOGLE_AI_KEY'])

    def generate_text(self, prompt: str = "The opposite of hot is"):
        response = palm.generate_text(prompt=prompt)
        return response.result  # Outputs: 'cold.'

    def generate_exercise(self, age, difficulty, scenario, character):
        # Generate the prompt for the exercise
        prompt = f"""
            You are a friendly math tutor specializing in teaching young children, 
            specifically {age}-year-olds, the basics of arithmetic in a fun and engaging way. 
            Your goal is to create a simple and enjoyable arithmetic exercise 
            that helps a {age}-year-old understand age-appropriate arithmetic. The exercise should involve arithmetic 
            of two small numbers.
            write story followed by an exercise framed in an imaginary setting of {scenario} and the main character
            is {character}. response in json"""

        # Generate text using GPT4All
        response = self.generate_text(prompt=prompt)
        processed_response = self.process_response(response)
        return processed_response

    def process_response(self, response):
        try:
            # Clean the response string
            # Remove leading and trailing non-JSON characters (like backticks or 'json' markers)
            cleaned_response = response.strip("`")

            # Parse the cleaned JSON string
            parsed_response = json.loads(cleaned_response)

            # Return the parsed JSON as a dictionary
            return parsed_response
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            print("Failed to decode JSON:", e)
            return response
