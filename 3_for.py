"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [
{'school_class_01': '1A', 'number_pupils': 7, 'on_work': 5, 
'on_sickleave': 2,'pupils_scores':[3,4,5,5,3]},

{'school_class_02': '1B', 'number_pupils': 5, 'on_work': 5, 
'on_sickleave': 0, 'pupils_scores':[5,5,5,5,4]},

{'school_class_03': '1C', 'number_pupils': 6, 'on_work': 5, 
'on_sickleave': 1, 'pupils_scores':[3,4,4,4,3]} 
]

def main(schl = school, on_wrk = school, ppls_scrs = school):
    for ppls_scrs in schl:
        avrg_schl = ppls_scrs / on_wrk
        return(avrg_schl)
    
#def each_class(school, school_class_01, school_class_02, school_class_03,
#number_pupils, on_work, on_sickleave, pupils_scores):
#    for 
    
if __name__ == "__main__":
    main()

#if __name__ == "__each_class__":
#    each_class()    

total_school = main(school)
#total_class = each_class()

print(total_school) # total_class)

'''
print(school[1])
'''