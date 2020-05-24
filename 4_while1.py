"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
user_ask = input()

def ask_user(robot_question = "Как дела?", user = input(), 
those_answer = 'Хорошо'):
    while user != those_answer:
        return(robot_question)
    if user == those_answer:
        return('Пока!')

if __name__ == "__ask_user__":
    ask_user()
