import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')


I=tk.Label(window,bg='yellow',width=20,height=3,text='empty')
I.pack()

def print_selection():
    if(var1.get() == 1)&(var2.get() == 0):
        I.config(text='I love only Python')
    elif(var1.get() == 0)&(var2.get() ==1 ):
        I.config(text='I love only C++')
    elif(var1.get() == 1)&(var2.get() ==1 ):
        I.config(text='I love both')
    else:
        I.config(text='I do not love either')

var1=tk.IntVar()
var2=tk.IntVar()
c1=tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,
                  command=print_selection)
c2=tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,
                  command=print_selection)
c1.pack()
c2.pack()


#window會不斷刷新，while loop
window.mainloop()
