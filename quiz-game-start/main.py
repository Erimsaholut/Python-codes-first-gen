from data import question_data, new_data
from question_model import NewQuestion
from quiz_brain import QuizzBrain
question_bank = []
for i in range(len(new_data[0]["results"])):
    qt = new_data[0]["results"][i]["question"]
    qa = new_data[0]["results"][i]["correct_answer"]
    question_bank.append(NewQuestion(qt, qa))

a = QuizzBrain(question_bank)
a.next_question()

while a.still_has_questions():
    a.next_question()










