"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
user_age = int(input('Пожалуйста, введите ваш возраст: '))

def main(user_age):
    if user_age <= 6:
        return('Вы ещё ходите в детский сад.')
    elif 6 <= user_age <= 16:
        return('Вы ходите в начальную или среднюю школу.')
    elif 16 <= user_age <= 23:
        return('Вы учитесь в университете.')
    elif user_age > 23:
        return('Вы уже работаете.')

if __name__ == "__main__":
    main(user_age)
resolution = main(user_age)
print(resolution)
