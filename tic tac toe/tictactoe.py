from tkinter import ttk
from tkinter import *
from tkinter import messagebox
window=Tk()
frame=ttk.Frame(window)
frame.grid()
lab=ttk.Label(frame,text="its X move")
lab.grid(row=0,column=0)
buttons=[]
turn="O"
ct=0
arr=[0,0,0,0,0,0,0,0,0]
def check(turn):
    for i in range(3):
        if(buttons[i][0].cget("text")==buttons[i][1].cget("text") and buttons[i][0].cget("text")==buttons[i][2].cget("text") and buttons[i][2].cget("text")==turn):
            return True
    for i in range(3):
        if(buttons[0][i].cget("text")==buttons[1][i].cget("text") and buttons[0][i].cget("text")==buttons[2][i].cget("text") and buttons[2][i].cget("text")==turn):
            return True
    if(buttons[0][0].cget("text")==buttons[1][1].cget("text") and buttons[0][0].cget("text")==buttons[2][2].cget("text") and buttons[2][2].cget("text")==turn):
        return True
    if(buttons[0][2].cget("text")==buttons[1][1].cget("text") and buttons[0][2].cget("text")==buttons[2][0].cget("text") and buttons[2][0].cget("text")==turn):
        return True
    return False
def config(a,b):
    global ct
    global turn
    if ct<9:
        if arr[a*3+b]:
            lab.config(text="already used!!")
        else:
            lab.config(text=("its "+turn+" move"))
            if(turn=="X"):
                turn="O"
            else:
                turn="X"
            buttons[a][b].config(text=turn)
            arr[a*3+b]=1
            ct+=1
            a=check(turn)
            if a:
                messagebox.showinfo("Information",turn+" Won!!")  
                window.destroy()
            elif ct==9:
                messagebox.showinfo("Information","Its Draw!!")  
                window.destroy()
                
                
def matrix_view():
    #global buttons
    for i in range(3):
        button=[]
        for j in range(3):
            but=ttk.Button(frame,text="",command=lambda a=i,b=j:config(a,b))
            but.grid(row=i+1,column=j)
            button.append(but)
        buttons.append(button)

matrix_view()
window.mainloop()