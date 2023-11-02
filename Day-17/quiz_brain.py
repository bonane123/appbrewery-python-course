
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print(f"You got it right! Your score is")

        else:
            print(f"That's wrong! Your score is")
        print(f"The answer was: {current_answer}.")
        print(f"Your current score is: {self.score}/ {self.question_number}")
        print("\n")

    def final_score(self):
        print("You've completed the quiz")
        print(f"Your final score is: {self.score}/ {self.question_number}")