from tkinter import *
from tkinter import ttk
class ToDoList:
    def __init__(self,root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('630x400+305+150')
                   
        
        self.label = Label(self.root,text='To-Do-List!!',font=('times new roman',30,'bold'),height=2,width=10,bd=5,bg='pink',fg='black')
        self.label.pack(side='top',fill=BOTH)

        self.label2 = Label(self.root,text='Add Task',font=('times new roman',20,'bold'),width=10,bd=5,bg='pink',fg='black')
        self.label2.place(x=30,y=130)

        self.label3 = Label(self.root,text='Tasks',font=('times new roman',20,'bold'),width=10,bd=5,bg='pink',fg='black')
        self.label3.place(x=370,y=94)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23,font=('ariel',20,'italic bold'))
        self.main_text.place(x=290,y=140)

        self.text = Text(self.root, bd=5, height=2, width=23, font=('ariel',14,'bold'))
        self.text.place(x=40,y=180)

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt','r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line :
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)
            with open('data.txt','r') as file:
                read = file.readlines()
                for i in read:
                    ready = i.split()
                    self.main_text.insert(END,ready)
                file.close()    

        self.button = Button(self.root, text="Add",font=('sarif', 25,'bold'),width=10, bd=5 ,bg='pink', fg='black', command=add)
        self.button.place(x=40,y=240)

        self.button2 = Button(self.root, text="Delete", font=('arial',25,'bold'),width=10,bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=40,y=300)

        

def main():
    root = Tk()
    ui = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()    
