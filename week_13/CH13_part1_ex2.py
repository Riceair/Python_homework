import json

python_obj = {
    "id" : "A1065506",
    "class" : "CSIE",
    "year" : 3
}
#一開始type為dict
print("一開始type為dict\n"+str(type(python_obj)))

json_obj = json.dumps(python_obj)
#轉成json object會變成string
print("\n轉成json後會變成string\n"+str(type(json_obj)))
print(json_obj)
