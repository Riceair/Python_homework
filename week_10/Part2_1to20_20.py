thedict = [{"V0":"S000"},{"V1":"S001"},{"V2":"S002"}]

print(thedict)

val_list = [val for dic in thedict for val in dic.values()]

print(val_list)
