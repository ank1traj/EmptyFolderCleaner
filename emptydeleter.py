#DELETE  EMPTY FOLDERS
from tkinter import *
import os

def clean():
    b,c=[],0
    for root, directories, filenames in os.walk(str(E1.get())):
        for directory in directories:
            b.append(os.path.join(root, directory))
    for i in b:
        try:
            os.rmdir(i)
            c=c+1
        except  OSError:
            pass
    return c
def show():
    show=str(clean())
    show=show+' Empty files deleted.\n'
    T.insert(END,show)

window=Tk()
window.geometry('500x500')
window.title('Empty Folder Cleaner')
l1=Label(text='Empty Folder Cleaner',font=('Times New Roman',20),bg='red',fg='white',width=35,height=1,anchor=N)
l1.grid()
l2=Label(text='Enter Directorie path \nto Delete all Empty Files:',font=('Courier New',19))
l2.grid()
E1=Entry(width='40',bg='Gray',fg='white')
E1.grid()
B=Button(text='Clean Junk',bg='brown',fg='white',command=show)
B.grid()
T=Text(width=40,font=('verdana',12))
T.grid()
window.mainloop()
