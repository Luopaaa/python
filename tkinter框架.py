import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

tk.Label(window,text='on the window').pack()
frm=tk.Frame(window)
frm.pack()

frm_1=tk.Frame(frm)
frm_2=tk.Frame(frm)
frm_1.pack(side='left')#side決定方向
frm_2.pack(side='right')

tk.Label(frm_1,text='on the frm_1').pack()
tk.Label(frm_1,text='on the frm_2').pack()
tk.Label(frm_2,text='on the frm_3').pack()

#window會不斷刷新，while loop
window.mainloop()
