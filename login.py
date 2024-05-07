from tkinter import *
from tkinter import messagebox
root=Tk()


root.configure(bg='cyan4')
label1 = Label(root, text='Login page', bg='white', fg='red', font=('Arial', 20))
label1.place(x=110, y=100)
label2=Label(root,text='UserName:',font=('Areal',20),bg='white')
label2.place(x=110,y=220)
label3=Label(root,text='Password:',font=('Areal',20),bg='white')
label3.place(x=110,y=330)
entry1=Entry(root,font=('Areal',20,))
entry1.place(x=260,y=220)
entry2=Entry(root,font=('Areal',20,))
entry2.place(x=260,y=330)
root.mainloop()
