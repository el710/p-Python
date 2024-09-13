import tkinter
from tkinter import filedialog
import os
import tkinter.filedialog

filename =  None

def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=( ("text file", ".txt"), 
                                                     ("all files", "*") ))
    text['text'] = f"{text['text']} {filename}"
    text['width'] = len(filename)
    #os.startfile(filename)
    _file = open(filename, 'r', encoding='utf-8')
    fd['text'] = _file.read()
    _file.close()


def info_view():
    pass

def about_view():
    pass


window = tkinter.Tk()

window.title("Explorer")
window.geometry('350x500')
window.resizable(False, False)
window.configure(background='gray')

menubar = tkinter.Menu(window)
file = tkinter.Menu(menubar, tearoff=0)
file.add_command(label="Open", command=file_select)
file.add_separator()
file.add_command(label="Exit",command=window.quit)
menubar.add_cascade(label="File", menu=file)

about = tkinter.Menu(menubar, tearoff=0)
about.add_command(label="Info", command=info_view)
about.add_separator()
about.add_command(label="About", command=about_view)
menubar.add_cascade(label="About", menu=about) 

window.config(menu=menubar)

text = tkinter.Label(window, text='File:', height=5, background='silver')
#text.grid(column=1, row=1)
text.pack(side='top', fill='x')

button_select = tkinter.Button(window, width=50, height=3, text='Choose file', command=file_select, foreground='blue')
#button_select.grid(column=1, row=2)
button_select.pack(anchor='n', fill='x')

fd = tkinter.Label(window, background='white')
#text.grid(column=1, row=1)
fd.pack(expand=True, side='bottom', fill='both')



window.mainloop()