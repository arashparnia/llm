from service.factories.ContentFactory import ContentFactory
import logging

class GoogleGenerativeAIServiceFactory(ContentFactory):
    def __init__(self, google_generative_ai_service):
        self.google_generative_ai_service = google_generative_ai_service

    def generate_story(self, scenario, characters, genre):
        # Implementation using GoogleGenerativeAIService
        pass

    def generate_exercise(self, age, difficulty, scenario, character):
        prompt = f"""
            Generate an educational exercise suitable for a {age}-year-old student. 
            The exercise should be at a '{difficulty}' level, themed around '{scenario}', 
            and involve the character '{character}'. The exercise should test basic arithmetic skills.
        """

        # Log the constructed prompt
        logging.info("Constructed Prompt: %s", prompt)

        # Print the prompt (useful for debugging)
        print("Constructed Prompt:", prompt)

        exercise_text = self.google_generative_ai_service.generate_text(prompt)

        # Log the response
        logging.info("Generated Exercise Text: %s", exercise_text)

        # Print the response (useful for debugging)
        print("Generated Exercise Text:", exercise_text)

        return exercise_text

    def generate_multiple_choice_question(self, subject, topic, difficulty):
        # Implementation using GoogleGenerativeAIService
        pass
