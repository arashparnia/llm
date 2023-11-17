import json

from PIL import Image, ImageDraw, ImageFont

from models.Completion import ChatMessage
from service.ChatGPTService import ChatGPTService


class ExerciseGenerator:
    def __init__(self):
        self.chat_gpt_service = ChatGPTService()

    def generate_exercise(self, age, difficulty, scenario, character):
        # Step 1: Generate text based on the input scenario and character using ChatGPTService
        messages = [
            {"role": "system", "content": f"""
               you will generate a text problem should have enough details and context for dall-e 3 model to 
               generate an accurate image for it. 
               You are a friendly math tutor specializing in teaching young children, 
               specifically {age}-year-olds, the basics of arithmetic in a fun and engaging way. 
               Your goal is to create a simple and enjoyable arithmetic exercise 
               that helps a {age}-year-old understand age appropriate arithmetic. 
               The exercise should involve arithmetic of two small numbers.
               The problem will vary in difficulty 
               but even the highest difficulty should be appropriate for a {age}-year-old  child.
               please set the difficulty to {difficulty}. reply with a json of the problem itself and the answer.

               """},
            {"role": "user", "content": f"""write an exercise framed in an imaginary {scenario} and the main character 
            is {character}. """}
        ]

        response = self.chat_gpt_service.create_chat_completion(model="gpt-3.5-turbo-1106", messages=messages)
        print(response)

        # Extract the content of the assistant's message
        assistant_message = response['choices'][0]['message']['content']

        # Parse the content as JSON to access 'problem' and 'answer'
        parsed_content = json.loads(assistant_message)
        problem = parsed_content.get('problem', '')
        answer = parsed_content.get('answer', '')

        print(f"Problem: {problem}")
        print(f"Answer: {answer}")
        print(response['usage'])

        # Step 2: Generate an image from the generated text (replace with your image generation logic)
        generated_image_url = self.chat_gpt_service.create_image(problem)

        # Step 3: Generate audio voice from the generated text using ChatGPTService
        generated_audio_data = self.chat_gpt_service.create_speech(problem)

        # Package the exercise text, answer, image, and audio
        exercise = {
            "exercise": problem,
            "answer": answer,
            "image": generated_image_url,  # Image object
            "audio": generated_audio_data,  # Audio data as bytes
        }

        return exercise

