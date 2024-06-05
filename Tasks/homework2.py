#home work "Variables"

import os
os.system('cls')

Count_Task = int(input("Input quantity of solved tasks: "))
Count_Time = int(input("Input quantity of spent hours: "))
Course_Name = input("Type name of your course: ")

Time_Per_Task = round(Count_Time / Count_Task, 5)

print(f'So, on course "{Course_Name}"')
print("you had", Count_Task, "tasks", "and spent", Count_Time, "hours")
print("and have been using", Time_Per_Task, "hour per task")


input("Press <Enter> for end...")
# end of task 2