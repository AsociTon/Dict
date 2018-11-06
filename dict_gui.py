from tkinter import*
import json
import difflib
from difflib import get_close_matches


window = Tk()

data = json.load(open("data.json"))

def find_word():
    t1.delete("0.1",END)
    key = e1_var.get()
    key = key.lower()#gets the input in lower case
    if key in data:
        for i in data[key]:
            t1.insert(END,i)
#    elif len(get_close_matches(key,data))>0:
#        print("Did you mean "+get_close_matches(key,data)[0]+" instead!")
#        choi = input("yes/no:")
#        choi = choi.lower()
#        if choi == "yes":
#            key = get_close_matches(key,data)[0]
#            for i in data[key]:
#                print(i)
#        else:
#            print("Sorry we do not have such word !(")
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
