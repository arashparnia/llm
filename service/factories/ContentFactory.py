from abc import ABC, abstractmethod

class ContentFactory(ABC):
    @abstractmethod
    def generate_story(self, scenario, characters, genre):
        pass

    @abstractmethod
    def generate_exercise(self, age, difficulty, scenario, character):
        pass

    @abstractmethod
    def generate_multiple_choice_question(self, subject, topic, difficulty):
        pass
