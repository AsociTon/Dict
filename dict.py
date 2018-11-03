import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))

def find_word():
    key = input("Enter word ypu want to search for:")
    key  = key.lower()#gets the input in lower case
    count = 0 #can use key.title() to capitalize the first alphabet
    key1 = ""
    for i in key:
        if count == 0:
            key1 += i.upper()
        else:
            key1 += i
        count += 1
    if key in data:
        for i in data[key]:
            print(i)
    elif key1 in data:
        for i in data[key1]:
            print(i)
    elif key.upper() in data:
         for i in data[key.upper()]:
             print(i)        
    elif len(get_close_matches(key,data))>0:
        print("Did you mean "+get_close_matches(key,data)[0]+" instead!")
        choi = input("yes/no:")
        choi = choi.lower()
        if choi == "yes":
            key = get_close_matches(key,data)[0]
            for i in data[key]:
                print(i)
        else:
            print("Sorry we do not have such word !(")
    else:
        print("word not present in dictionary :(")

find_word()
