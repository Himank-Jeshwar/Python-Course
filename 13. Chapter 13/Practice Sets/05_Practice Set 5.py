from functools import reduce
maximum=lambda a,b:max(a,b)
l=[45,12,34,56,23,32,78,21,54,90,13,14,51,620,97]
findMax=reduce(maximum,l)
print(f"Greatest Number = {findMax}")