class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0

    def still_has_questions(self):
        return self.question_number <= len(self.question_list)-1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number} {current_question.text} (True\False)")
        correct_answer = current_question.answer
        self.check_answer(user_input, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right !")
            self.user_score += 1
        else:
            print("That's wrong")
            print(f"The correct answer is {correct_answer}.")
        print(f"Your score is {self.question_number}/{self.user_score}\n")
        self.game_finish()

    def game_finish(self):
        if not self.still_has_questions():
            print("You've completed the quiz")
            print(f"Your final score is: {self.question_number}/{self.user_score}")