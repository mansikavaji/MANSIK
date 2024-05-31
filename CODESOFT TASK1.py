import tkinter
from tkinter import *


root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]
def addTask():
    task= task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a')as taskfile:
            taskfile.write(f"\n{task})
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task = str(listbox,get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w')as taskfile:
         for task in task_list:
             taskfile,write(task+"\n")

        listbox.delete(ANCHOR)
             

def openTaskFile():
    try:
        global task_list
        with open("tasklist.text","r")as taskfile:
          tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()
#icon
Image_icon=PhotoImage(file="image/C:\Users\mansi\AppData\Local\Programs\task.png")
root.iconphoto(false,Image_icon)

#top bar
TopImage=PhotoImage(file="image/C:\Users\mansi\AppData\Local\Programs\topbar.png")
label(root,image=TopImage).pack()

dockImage=PhotoImage(file="image/C:\Users\mansi\AppData\Local\Programs\topbar.png")
label(root,image=dockImage,bg="#32405b"),place(x=30,y=25)

noteImage=PhotoImage(file="Image/C:\Users\mansi\AppData\Local\Programs\task.png")
label(root,image=noteImage,bg="#32405b").place(x=30,y=25)

heading=label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

#main
frame=frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

tasl=stringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0
task_entry.place(x=10,y=7)
task_entry.focus
                 
button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a9ff",fg="fff",bd=0)
button.place(x=300,y=0)

#listbox
frame1=Frame(root,bd=3,width=700,height=280,bg="#32405")
frame1.pack(pady=(160,0)


listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405",fg="white",cursor="hand2",select)
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=scrolbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrolbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon=PhotoImage(file="Image/C:\Users\mansi\AppData\Local\Programs\delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
root.mainloop()
