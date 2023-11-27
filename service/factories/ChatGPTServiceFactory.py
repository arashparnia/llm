from service.factories.ContentFactory import ContentFactory


class ChatGPTServiceFactory(ContentFactory):
    def __init__(self, chat_gpt_service):
        self.chat_gpt_service = chat_gpt_service

    def generate_story(self, scenario, characters, genre):
        # Implementation using ChatGPTService
        pass

    def generate_exercise(self, age, difficulty, scenario, character):
        # Implementation using ChatGPTService
        pass

    def generate_multiple_choice_question(self, subject, topic, difficulty):
        # Implementation using ChatGPTService
        pass
