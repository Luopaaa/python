import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    #tk.messagebox.showinfo(title='Hi',message='hahahahaha')
    #tk.messagebox.showwarning(title='Hi',message='nonononono')
    #tk.messagebox.showerror(title='Hi',message='xxxxxxx')
    #print(tk.messagebox.askquestion(title='Hi',message='hahahahaha'))  #return yes,no
    #print(tk.messagebox.askyesno(title='Hi',message='hahahahaha'))  #return Ture,False
    #print(tk.messagebox.asktrycancel(title='Hi',message='hahahahaha'))
    print(tk.messagebox.askokcancel(title='Hi',message='hahahahaha'))
tk.Button(window,text='hit me',command=hit_me).pack()



#window會不斷刷新，while loop
window.mainloop()
