from ChatGPT import ChatGPT
from mathtutor import MathTutor

def main():
    chat_gpt = ChatGPT()  # Ensure ChatGPT is initialized with the necessary API key
    tutor = MathTutor(chat_gpt)

    while True:
        problem = tutor.generate_problem()
        print(f"Solve: {problem}")

        tutor.start_timer()
        user_answer = input("Your answer: ")  # Assume the user enters a valid answer
        tutor.stop_timer()

        correct_answer = tutor.get_solution(problem)
        correctness, time_taken = tutor.evaluate_performance(user_answer, correct_answer)
        tutor.adjust_difficulty(correctness, time_taken)

        feedback = "Correct!" if correctness else f"Incorrect. The correct answer is {correct_answer}."
        print(f"{feedback} Time taken: {time_taken:.2f} seconds. Difficulty level: {tutor.difficulty}\n")

if __name__ == "__main__":
    main()
