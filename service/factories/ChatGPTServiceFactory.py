from service.factories.ContentFactory import ContentFactory


class ChatGPTServiceFactory(ContentFactory):
    """
     Factory class for generating educational content using ChatGPTServiceFactoryservice.

     This class provides methods to generate stories, exercises, and multiple-choice questions
     tailored to specific age groups, difficulty levels, scenarios, and characters.

     Attributes:
         ChatGPT_Service_Factory: An instance of the ChatGPTServiceFactoryservice class
                                       used for content generation.
     """

    def __init__(self, chatgpt_service):
        """
              Initializes the chatgpt_service with a chatgpt_service service instance.

              Args:
                  chatgpt_service: An instance of a chatgpt_service service class.
              """
        self.chatgpt_service = chatgpt_service

    def generate_story(self, scenario, characters, genre):
        """
        Generates a story based on the provided scenario, characters, and genre.

        Args:
            scenario (str): The scenario or setting for the story.
            characters (str): The characters involved in the story.
            genre (str): The genre of the story.

        Returns:
            str: The generated story.
        """
        user_message = f"Generate a story based on the scenario: {scenario}, characters: {characters}, and genre: {genre}"
        thread = self.chatgpt_service.create_thread()
        self.chatgpt_service.create_message(thread_id=thread['id'], content=user_message)
        run = self.chatgpt_service.create_run(thread_id=thread['id'])
        self.chatgpt_service.wait_for_run_completion(thread_id=thread['id'], run_id=run['id'])
        messages = self.chatgpt_service.list_messages(thread_id=thread['id'])
        assistant_response = next((m['content'] for m in messages if m['role'] == 'assistant'), None)
        return assistant_response

    def generate_exercise(self, age, difficulty, scenario, character):
        """
        Generates a text-based exercise based on age, difficulty level, scenario, and character.

        Args:
            age (int): The targeted age group for the exercise.
            difficulty (str): The difficulty level of the exercise.
            scenario (str): The scenario or context for the exercise.
            character (str): The character involved in the exercise.

        Returns:
            str: The generated exercise.
        """
        exercise_prompt = f"Create an exercise for age {age}, difficulty {difficulty}, based on the scenario {scenario} and character {character}."
        thread = self.chatgpt_service.create_thread()
        self.chatgpt_service.create_message(thread_id=thread['id'], content=exercise_prompt)
        run = self.chatgpt_service.create_run(thread_id=thread['id'])
        self.chatgpt_service.wait_for_run_completion(thread_id=thread['id'], run_id=run['id'])
        messages = self.chatgpt_service.list_messages(thread_id=thread['id'])
        exercise = next((m['content'] for m in messages if m['role'] == 'assistant'), None)
        return exercise

    def generate_multiple_choice_question(self, subject, topic, difficulty):
        """
        Generates a multiple-choice question based on a given subject, topic, and difficulty level.

        Args:
            subject (str): The subject area of the question.
            topic (str): The specific topic within the subject area.
            difficulty (str): The difficulty level of the question.

        Returns:
            str: The generated multiple-choice question.
        """
        question_prompt = f"Create a multiple-choice question about {topic} in {subject} at {difficulty} level."
        thread = self.chatgpt_service.create_thread()
        self.chatgpt_service.create_message(thread_id=thread['id'], content=question_prompt)
        run = self.chatgpt_service.create_run(thread_id=thread['id'])
        self.chatgpt_service.wait_for_run_completion(thread_id=thread['id'], run_id=run['id'])
        messages = self.chatgpt_service.list_messages(thread_id=thread['id'])
        question = next((m['content'] for m in messages if m['role'] == 'assistant'), None)
        return question
