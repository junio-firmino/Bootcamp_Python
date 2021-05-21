class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.user_answer = str

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        #global self.user_answer
        flag = True
        while flag:
            self.user_answer = input(f'Q.{self.question_number}: {current_question.text} (true or false)?')
            if self.user_answer != 'true' and self.user_answer != 'false':
                print("We haven't this options, Please give us another opinion")

            else:
                flag = False

        self.check_answer(user_answer=self.user_answer, current_question=current_question.answer)
        print(f'Your score at moment is {self.score}/{self.question_number}')



    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            self.analize(score_final=self.score)
            return False

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.lower():
            print('Excelente you are correct!.')
            self.score += 1
        else:
            print('Unfortunately you made mistake.')
        print(f'correct answer is {current_question}')

    def analize(self, score_final):
        if score_final < 5:
            print('You are low level in this topic, You should improve your knowledge.')
        elif score_final >= 5 and score_final < 8:
            print('You are median level in this topic, Try read more for improve more and more.')
        else:
            print('You are high, Keep going this way.')
