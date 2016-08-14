import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
I=tk.Label(window,bg='yellow',width=20,height=3,text='empty')
I.pack()

def print_selection():
    I.config(text='you have select'+var.get())

r1=tk.Radiobutton(window,text='Option A',variable=var,value='A',command=
                  print_selection)
r1.pack()

r2=tk.Radiobutton(window,text='Option B',variable=var,value='B',command=
                  print_selection)
r2.pack()

r3=tk.Radiobutton(window,text='Option C',variable=var,value='C',command=
                  print_selection)
r3.pack()



#window會不斷刷新，while loop
window.mainloop()
