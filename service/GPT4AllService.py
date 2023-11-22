from gpt4all import GPT4All
import json
class GPT4AllWrapper:
    def __init__(self, model_name):
        self.model = GPT4All(model_name)

    def generate_text(self, prompt, max_tokens=50):
        output = self.model.generate(prompt, max_tokens=max_tokens)
        return output


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
        response = self.generate_text(prompt, max_tokens=500)
        return response

        # # Extract the problem and the answer
        # parsed_content = json.loads(response)
        # problem = parsed_content.get('problem', '')
        # answer = parsed_content.get('answer', '')
        #
        # print(f"Problem: {problem}")
        # print(f"Answer: {answer}")
        #
        # # Steps for generating the image and audio can be added here as before
        # # ...
        #
        # # Package the exercise components
        # exercise = {
        #     "exercise": problem,
        #     "answer": answer,
        #     # Add image and audio once generated
        # }
        #
        # return exercise
