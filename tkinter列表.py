import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
I=tk.Label(window,bg='yellow',width=4,height=2,textvariable=var1)
I.pack()


def print_selection():
    value = Ib.get(Ib.curselection())
    var1.set(value)



b1=tk.Button(window,text='print selection',width=15,height=2,command=print_selection)
b1.pack()

var2=tk.StringVar()
var2.set((11,22,44,33))
Ib=tk.Listbox(window,listvariable=var2)

list_items=[1,2,3,4]
for item in list_items:
    Ib.insert('end',item)

Ib.insert(1,'first')
Ib.insert(2,'second')
Ib.delete(2)
Ib.pack()

#window會不斷刷新，while loop
window.mainloop()
