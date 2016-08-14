import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')


I=tk.Label(window,bg='yellow',width=20,height=3,text='empty')
I.pack()

def print_selection(v):
    I.config(text='you have select'+ v)

s=tk.Scale(window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,length=300,
           showvalue=False,tickinterval=3,resolution=0.001,command=print_selection)

s.pack()

#window會不斷刷新，while loop
window.mainloop()
