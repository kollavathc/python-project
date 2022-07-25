from question_model import Question
from data import question_data, question_data_2
from quiz_brain import QuizBrain

# question_bank = []
#
# for i in range(len(question_data)):
#     question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
#
# # # other way
# # for question in question_data:
# #     question_text = question["text"]
# #     question_answer = question["answer"]
# #     new_question = Question(question_text, question_answer)
# #     question_data.append(new_question)
#
# quiz = QuizBrain(question_bank)
#
# while quiz.still_has_question():
#     quiz.next_question()
# print("You've completed the quiz.")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")


######################## QUESTION BANK 2 ############################

question_bank_2 = []

for i in range(len(question_data_2)):
    question_bank_2.append(Question(question_data_2[i]["question"], question_data_2[i]["correct_answer"]))

quiz = QuizBrain(question_bank_2)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

