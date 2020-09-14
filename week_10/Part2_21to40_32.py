thedict = {
    "Dan":{
        "ID":"A1065506",
        "year":1998
    },
    "Alex":{
        "ID":"B1234567",
        "year":2000
    }
}

for d in thedict:
    print(d)
    for vd in thedict[d]:
        print(vd,":",thedict[d][vd])
