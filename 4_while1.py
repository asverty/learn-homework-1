"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
def ask_user(question = 'Как дела?', user = input(), 
            answer = 'Хорошо'):
    while True:
        user != answer
        return question
    else:
        return('Пока!')

if __name__ == "__ask_user__":
    ask_user()
    user_ask = input()
print('Как дела?')
result = ask_user()
print(result)
