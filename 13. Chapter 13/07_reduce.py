from functools import reduce
total=lambda a,b:a+b
l1=[x for x in range(1,11)]
val=reduce(total,l1)
print(val)