divisible_by_5=lambda a:a%5==0
d5=[12,10,45,56,20,30,21,23,78,70,40,55,25,32]
print(f"Numbers of list that are divisible by 5 = {list(filter(divisible_by_5,d5))}")