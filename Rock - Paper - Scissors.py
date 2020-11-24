from tkinter import *
import random
b = None

def r():
    global b
    b = "Rock"

def p():
    global b
    b = "Paper"

def s():
    global b
    b = "Scissors"


def ans():
    global m
    if b in ("Rock", "Paper", "Scissors", "R", "P", "S", "r", "p", "s"):
        n = Label(root, text = m,font = "Courier")
        n.grid(row = 2, column = 1)
        if a == "Rock" and (b == "Scissors" or b == "S" or b == "s"):
            q = Label(root, text = o,font = "Courier")
            q.grid(row = 3, column = 1)
        elif a == "Rock" and (b == "Paper" or b == "P" or b == "p"):
            r = Label(root, text = j,font = "Courier")
            r.grid(row = 3, column = 1)
        elif a == "Scissors" and (b == "Paper" or b == "P" or b == "p"):
            q = Label(root, text=o,font = "Courier")
            q.grid(row = 3, column = 1)
        elif a == "Scissors" and (b == "Rock" or b == "R" or b == "r"):
            r = Label(root, text=j,font = "Courier")
            r.grid(row = 3, column = 1)
        elif a == "Paper" and (b == "Rock" or b == "R" or b == "r"):
            q = Label(root, text=o,font = "Courier")
            q.grid(row = 3, column = 1)
        elif a == "Paper" and (b == "Scissors" or b == "S" or b == "s"):
            r = Label(root, text=j,font = "Courier")
            r.grid(row = 3, column = 1)
        else:
            l = Label(root, text = k,font = "Courier")
            l.grid(row = 3, column = 1)
    else:
        i = Label(root, text = "Please Enter a Valid Input!",font = "Courier")
        i.grid(row = 3, column = 1)
root = Tk()
root.title("Get Ready to Play Rock, Paper, Scissors with Game-O-Champ!!!")
rand = ["Rock", "Paper", "Scissors"]
a = random.choice(rand)
m = "Computer's Choice: " + a
o = "Better Luck Next Time!!"
j = "Congratulations!! You Won!!"
k = "It's a draw!!"

root.geometry("950x325+400+100")
r1 = Button(root, text = "Rock", relief=RIDGE,bg="yellow",bd=5,width = 30, height = 3, fg='red',font = "Courier", command = r)
p1 = Button(root, text = "Paper", relief=RIDGE,bg="yellow",bd=5,width = 30, height = 3,fg='red',font = "Courier", command = p)
s1 = Button(root, text = "Scissors", relief=RIDGE,bg="yellow",bd=5,width = 30, height = 3,fg='red',font = "Courier", command = s)
ans1 = Button(root, text = "Calculate Result",relief=RIDGE,bg="blue",width = 30, height = 3,bd=5,fg='yellow',font = "Courier", command = ans)
r1.grid(row = 0, column = 0)
p1.grid(row = 0, column = 1)
s1.grid(row = 0, column = 2)
ans1.grid(row = 1, column = 1)
root.mainloop()