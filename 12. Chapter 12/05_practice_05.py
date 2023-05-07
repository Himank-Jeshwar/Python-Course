num=int(input("Enter a number = "))
table=[num*i for i in range(1,11)]
print(table)
with open("tables.txt","a") as d:
        d.write(str(table))
        d.write("\n")