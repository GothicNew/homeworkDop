# Задание "Средний балл":
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#for el in grades:
#    average = [sum(el) / len(el)]
#    print(average)

average = [sum(el)/len(el) for el in grades]
print(average)

students = list(students)
students.sort()
print(students)

classbook = {}

for i in range(len(average)):
    classbook[students[i]] = [average[i]]

print(classbook)















