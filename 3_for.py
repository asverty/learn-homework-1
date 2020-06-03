"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def main(scrs, wrk):
    for scrs in school:
        sum_result = 0
        avg_schl = sum_result + sum(scrs) / wrk
        return(avg_schl)
	for scrs in classes:
        sum_result = 0
        avg_clss = sum_result + scrs / wrk
		return(avg_clss)

school = [
{
	'class_01': '1A',
	'num_pupils': 7, 
	'work': 5, 
	'sick': 2,
	'scores':[3,4,5,5,3]
},
{
	'class_02': '1B',
	'num_pupils': 5, 
	'work': 5, 
	'sick': 0, 
	'scores':[5,5,5,5,4]
},
{
	'class_03': '1C', 
	'num_pupils': 6, 
	'work': 5, 
	'sick': 1, 
	'scores':[3,4,4,4,3]
}]

if __name__ == "__main__":
	main()
	
	result_school = main
	(
	sum(school[0].get('scores') 
	+ school[1].get('scores') 
	+ school[2].get('scores')), 
	(school[0].get('work') 
	+ school[1].get('work') 
	+ school[2].get('work')
	)
	
	result_class_1A = main
	(school[0].get('scores'), school[0].get('work'))

	result_class_1B = main
	(school[1].get('scores'), school[1].get('work'))

	result_class_1C = main
	(school[2].get('scores'), school[2].get('work'))


	print(f'Средний балл по школе: {result_school}')

	print(f'Средний балл по классам: 
	1A {result_class_1A},
	1B {result_class_1B},
	1C {result_class_1C}')