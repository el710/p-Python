import os, statistics

os.system('cls')

## input data
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] 
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} 
print("We have grades: ", grades, type(grades))
print("and students: ", students, type(students))

# buffer_list = list(students)
# print("change type of student from set{} to list[]: ", buffer_list)

# # sort students
# buffer_list.sort()
# print("sort students: ", buffer_list)
##### or 

buffer_list = sorted(students)
print("listed & sorted students: ", buffer_list)

# make dictionary

# grades[0] = sum(grades[0]) / len(grades[0])
# grades[1] = sum(grades[1]) / len(grades[1])
# grades[2] = sum(grades[2]) / len(grades[2])
# grades[3] = sum(grades[3]) / len(grades[3])
# grades[4] = sum(grades[4]) / len(grades[4])
### or 
# grades[0] = statistics.mean(grades[0])
# grades[1] = statistics.mean(grades[1])
# grades[2] = statistics.mean(grades[2])
# grades[3] = statistics.mean(grades[3])
# grades[4] = statistics.mean(grades[4])
### or
for i in range(len(grades)):
    grades[i] = statistics.mean(grades[i])

# ave = sum(grades[0]) / len(grades[0])
# name = buffer_list[0]
# average.update({name: ave})

# ave = sum(grades[1]) / len(grades[1])
# name = buffer_list[1]
# average.update({name: ave})

# ave = sum(grades[2]) / len(grades[2])
# name = buffer_list[2]
# average.update({name: ave})

# ave = sum(grades[3]) / len(grades[3])
# name = buffer_list[3]
# average.update({name: ave})

# ave = sum(grades[4]) / len(grades[4])
# name = buffer_list[4]
# average.update({name: ave})

average = dict(zip(buffer_list, grades))

print("make dictionary of average grades: ", average)








input("\npress <Enter> to leave....")