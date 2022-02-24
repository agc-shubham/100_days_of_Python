from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    q_object = Question(q_text,q_answer)
    question_bank.append(q_object)

Quiz = QuizBrain(question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print('You have completed the quiz')
print(f'Your Final score is {Quiz.score}/{Quiz.question_number}')