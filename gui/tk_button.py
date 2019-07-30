import tkinter
top = tkinter.Tk()
top.title('this is a sample gui')
top.geometry('250x150')
quit1 = tkinter.Button(top ,text='click',command=top.quit)

quit1.pack()
tkinter.mainloop()
