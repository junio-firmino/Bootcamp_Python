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
            if not self.user_answer == 'true' or self.user_answer == 'false':
                print("We haven't this options, Please give us another opinion")
            else:
                flag = False

        self.check_answer(user_answer=self.user_answer, current_question=current_question.answer)
        print(f'Your score at moment is {self.score}/{self.question_number}')



    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.lower():
            print('Excelente you are correct!.')
            self.score += 1
        else:
            print('Unfortunately you made mistake.')
        print(f'correct answer is {current_question}')
