number=int(input("Enter any number = "))
mul_table=[number*b for b in range(1,11)]
print(mul_table)

f=open("tables.txt","a")
f.write(f"Multiplication of {number} = {mul_table}")
f.write("\n")
f.close()