# входные данные
grades = [
    [5,3,3,5,4],
    [2,2,2,3],
    [4,5,5,2],
    [4,4,3],
    [5,5,5,4,5]
]
students = {
    'Johny',
    'Bilbo',
    'Steve',
    'Khendrik',
    'Aaron'
}
# сортируем множество учеников и переводим в список
sorted_stud_list = list(sorted((list(students))))
# расчитываем список средних баллов
mid_grades = []
for el in grades:
    mid_grades.append(sum(el)/len(el))
# создание словаря с выходными данными
output_dist = dict(zip(sorted_stud_list,mid_grades))
# вывод словаря в консоль
print(output_dist)
