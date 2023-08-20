import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.geometry('500x500')

questions = ["who is father of python?","1+1=?","2+2=?","3+3=?","5+5=?"]
options= [['Guido Van Rossum','James Gosling','Dennis M.Rtchie','All The Above'],['A','B','2','c'],['A','4','2','B'],['H','N','6','C'],['6','3','10','8']]

frame = tk.Frame(root, padx=10,pady=10,bg='#fff')   
questions_label=tk.Label(frame,height=5,width=28,bg='#ddd',font=('times new roman',20,'bold'),wraplength=500)

v1=StringVar(frame)
v2=StringVar(frame)
v3=StringVar(frame)
v4=StringVar(frame)

option1 = tk.Radiobutton(frame,bg="#fff",variable=v1,font=('times new roman',20,'bold'),command=lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame,bg="#fff",variable=v2,font=('times new roman',20,'bold'),command=lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame,bg="#fff",variable=v3,font=('times new roman',20,'bold'),command=lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame,bg="#fff",variable=v4,font=('times new roman',20,'bold'),command=lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',font=('times new roman',20,'bold'),bg='black')
frame.pack(fill="both",expand = "true")
questions_label.grid(row=0,column=0)

option1.grid(sticky='W',row=1,column=0)
option2.grid(sticky='W',row=2,column=0)
option3.grid(sticky='W',row=3,column=0)
option4.grid(sticky='W',row=4,column=0)
button_next.grid(row=6,column=0)

index=0
correct=0
def disableButtons(state):
    option1['state']=state
    option2['state']=state
    option3['state']=state
    option4['state']=state
def checkAnswer(radio):
    global correct,index
    if radio['text']==options[index][4]:
        correct+=1
    index +=1
    disableButtons('disable')

def displayNextQuestion():
    questions_label['text']=questions[index]
    disableButtons('normal')
    opts=options[index]
    option1['text']=opts[0]
    option2['text']=opts[1]
    option3['text']=opts[2]
    option4['text']=opts[3]
    v1.set(opts[0])
    v2.set(opts[1])
    v3.set(opts[2])
    v4.set(opts[3])

    if index== len(options)-1:
        button_next['text']='check the results'

root.mainloop()
 