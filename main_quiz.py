from Day_17_dic_quiz import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text=question_text,q_answer=question_answer)
    question_bank.append(new_question)


quiz = Quizbrain(question_bank)
quiz.next_question()

