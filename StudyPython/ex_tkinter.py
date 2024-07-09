import tkinter as tk
import os

os.system('cls')


number_1 = ''
number_2 = ''
oper = ''
Turn_number = 0

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def get_str_values():
    num1 = number1_entry.get()
    num2 = number2_entry.get()
    return num1, num2

def show_res(value):
    result_entry.delete(0, 'end')
    result_entry.insert(0, value)

def show_exp():
   global number_1, number_2, oper
   exp_label.config(text=f"{number_1} {oper} {number_2}")

def add():
    global Turn_number, oper
    # num1, num2 = get_values()
    # res = num1 + num2
    # show_res(res)

    if Turn_number == 0:
       oper = '+'
       Turn_number = 1
    
    show_exp()

def sub():
    global Turn_number, oper

    if Turn_number == 0:
       oper = '-'
       Turn_number = 1
    
    show_exp()

def update_number1(value):
    global number_1
    number1_entry.delete(0, 'end')
    number1_entry.insert(0, str(value))
    number_1 = str(value)
    show_exp()

def update_number2(value):
    global number_2
    number2_entry.delete(0, 'end')
    number2_entry.insert(0, str(value))
    number_2 = str(value)
    show_exp()

def res():
   global number_1, number_2, oper, Turn_number

   num1, num2 = get_values()

   if oper == "+":
      res = num1 + num2
      show_res(res)
   elif oper == "-":
      res = num1 - num2
      show_res(res)
   elif oper == "/":
      res = num1 / num2
      show_res(res)
   else:
      res = num1 * num2
      show_res(res)

   exp_label.config(text=f"{number_1} {oper} {number_2} = ") 

   Turn_number = 0
   oper = ''
   number_1 = ''
   number_2 = ''
   number1_entry.delete(0, 'end')
   number2_entry.delete(0, 'end')

     

def set_one():
    global Turn_number

    if Turn_number == 0:
       if len(number1_entry.get()) < 1:
          numb = 1
       else: 
          numb = int(number1_entry.get()) * 10 + 1
      
       update_number1(numb)
    else:
       if len(number2_entry.get()) < 1:
          numb = 1
       else: 
          numb = int(number2_entry.get()) * 10 + 1
        
       update_number2(numb)
    
def set_two():
    global Turn_number

    if Turn_number == 0:
       if len(number1_entry.get()) < 1:
          numb = 2
       else: 
          numb = int(number1_entry.get()) * 10 + 2
      
       update_number1(numb)
    else:
       if len(number2_entry.get()) < 1:
          numb = 2
       else: 
          numb = int(number2_entry.get()) * 10 + 2
        
       update_number2(numb)

window = tk.Tk()
window.title('Calculator')
window.geometry('500x500')
window.resizable(False, False)


button_one = tk.Button(window, text=' 1 ', width=5, height=2, command=set_one)
##button_one.place(x=100, y=100)
button_one.grid(column=1, row=6)
button_two = tk.Button(window, text=' 2 ', width=5, height=2, command=set_two)
button_two.grid(column=2, row=6)
button_three = tk.Button(window, text=' 3 ', width=5, height=2, default='disabled')
button_three.grid(column=3, row=6)
button_four = tk.Button(window, text=' 4 ', width=5, height=2, default='disabled')
button_four.grid(column=1, row=7)
button_five = tk.Button(window, text=' 5 ', width=5, height=2, default='disabled')
button_five.grid(column=2, row=7)
button_six = tk.Button(window, text=' 6 ', width=5, height=2, default='disabled')
button_six.grid(column=3, row=7)
button_seven = tk.Button(window, text=' 7 ', width=5, height=2, default='disabled')
button_seven.grid(column=1, row=8)
button_eight = tk.Button(window, text=' 8 ', width=5, height=2, default='disabled')
button_eight.grid(column=2, row=8)
button_nine = tk.Button(window, text=' 9 ', width=5, height=2, default='disabled')
button_nine.grid(column=3, row=8)
button_pm = tk.Button(window, text='+/-', width=5, height=2, default='disabled')
button_pm.grid(column=1, row=9)
button_zero = tk.Button(window, text=' 0 ', width=5, height=2, default='disabled')
button_zero.grid(column=2, row=9)
button_point = tk.Button(window, text=' , ', width=5, height=2, default='disabled')
button_point.grid(column=3, row=9)

button_add = tk.Button(window, text='+', width=5, height=2, command=add)
button_add.grid(column=4, row=6)
button_sub = tk.Button(window, text='-', width=5, height=2, command=sub)
button_sub.grid(column=4, row=7)
button_mul = tk.Button(window, text='*', width=5, height=2, default='disabled')
button_mul.grid(column=4, row=8)
button_div = tk.Button(window, text='/', width=5, height=2, default='disabled')
button_div.grid(column=4, row=9)
button_eq = tk.Button(window, text='=', width=24, height=2, command=res)
button_eq.place(x=2, y=165)

exp_label = tk.Label(window, text='expression...', width=28)
exp_label.place(x=200, y=50)

number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=200, y=100)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=200, y=200)
result_entry = tk.Entry(window, width=28)
result_entry.place(x=200, y=300)


window.mainloop()

## to make exe need:
## install package:  pip install pyinstall (in terminal)
## > pyinstaller --onefile -w 'file.py'