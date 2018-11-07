from tkinter import*
import json
import difflib
from difflib import get_close_matches
from functools import partial

window = Tk()

window.title("Dictionary")

data = json.load(open("data.json"))


def choi1(key):
    key = get_close_matches(key,data)[0]
    for i in data[key]:
        t1.insert(END,i)
#    window2.destroy()
#    window2.mainloop()

def choi2(str):
    t1.delete("1.0",END)
    t1.insert(END,str)
#    window2.destroy()

def find_word():
    t1.delete("0.1",END)
    key = e1_var.get()
    key = key.lower()#gets the input in lower case
    if key in data:
        for i in data[key]:
            t1.insert(END,i)
    elif len(get_close_matches(key,data))>0:
        window2 = Tk()
        t2 = Text(window2,width = 25, height =2)
        t2.grid(row = 0, column = 0)

        bt1 = Button(window2, text = "Yes", command =lambda: choi1(key))
        bt1.grid(row = 1, column = 0)
        action_with_arg = partial(choi2,"Sorry we do not have such word !(")
        bt2 = Button(window2, text = "No", command = action_with_arg)
        bt2.grid(row = 1, column = 1)
        t2.delete("1.0", END)
        t2.insert(END, "Did you mean "+get_close_matches(key,data)[0]+" instead!")
#        if choi == "yes":
#            key = get_close_matches(key,data)[0]
#            for i in data[key]:
#                t1.insert(END,i)
#            window2.mainloop()
#        else:
#            t1.insert(END,"Sorry we do not have such word !(")
#            window2.mainloop()
    else:
        t1.insert(END,"word not present in dictionary :(")

e1_var = StringVar()

e1 = Entry(window, textvariable = e1_var)
e1.grid(row = 0, column = 0)

b1 = Button(window, text = "SEARCH", command = find_word)
b1.grid(row = 0, column = 1)

t1 = Text(window, width = 22, height = 22)
t1.grid(row = 1, column = 0,columnspan = 2)
#find_word()
window.mainloop()
