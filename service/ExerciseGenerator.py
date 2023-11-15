from PIL import Image, ImageDraw, ImageFont

from models.Completion import ChatMessage
from service.ChatGPTService import ChatGPTService


class ExerciseGenerator:
    def __init__(self):
        self.chat_gpt_service = ChatGPTService()

    def generate_exercise(self, age, difficulty, scenario, character):
        # Step 1: Generate text based on the input scenario and character using ChatGPTService
        prompt = f"""
               you will generate a text problem should have enough details and context for dall-e 3 model to 
               generate an accurate image for it. 
               You are a friendly math tutor specializing in teaching young children, 
               specifically {age}-year-olds, the basics of arithmetic in a fun and engaging way. 
               Your goal is to create a simple and enjoyable arithmetic exercise 
               that helps a {age}-year-old understand age appropriate arithmetic. 
               The exercise should involve arithmetic of two small numbers, 
               and it should be framed in an imaginary {scenario} and the main character is {character}.
               The problem will vary in difficulty 
               but even the highest difficulty should be appropriate for a {age}-year-old  child. 
               please set the difficulty to {difficulty}. reply with a json of the problem itself and the answer.

               """
        message = ChatMessage(prompt=prompt)
        response = self.chat_gpt_service.create_chat_completion(model="gpt-3.5-turbo-1106", messages=[message])
        generated_text = response['choices']['text']
        print(response['usage'])

        # Step 2: Generate an image from the generated text (replace with your image generation logic)
        generated_image_url = self.chat_gpt_service.create_image(generated_text)

        # Step 3: Generate audio voice from the generated text using ChatGPTService
        generated_audio_data = self.chat_gpt_service.create_speech(generated_text)

        # Package the exercise text, answer, image, and audio
        exercise = {
            "exercise": generated_text['exercise'],
            "answer": generated_text['answer'],
            "image": generated_image_url,  # Image object
            "audio": generated_audio_data,  # Audio data as bytes
        }

        return exercise
