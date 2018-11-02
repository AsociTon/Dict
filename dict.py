import json
data = json.load(open("data.json"))
key = input("Enter word ypu want to search for:")
if data[key]:
  for i in data[key]:
    print(i)
else:
 print("word not present!")
