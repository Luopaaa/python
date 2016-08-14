import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')




canvas=tk.Canvas(window,bg='yellow',height=100,width=200)

image_file=tk.PhotoImage(file='geor.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)

canvas.pack()

'''
b=tk.Button(window,text=move,command=moveit)
b.pack()
'''


#window會不斷刷新，while loop
window.mainloop()
