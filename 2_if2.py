"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
str_one = input('Введите превую строку: ')
str_two = input('Введите вторую строку: ')

def main(s_one = str_one, s_two = str_two, 
s_one_len = len(str_one), s_two_len = len(str_two)):
    if s_one == int() or s_two == int():
        return 0
    elif s_one == s_two:
        return 1
    elif s_one != s_two and s_one_len > s_two_len:
        return 2 
    elif s_one != s_two and s_two == 'learn':
        return 3

if __name__ == "__main__":
    main()
result = main()
print(result)

