# **\\
# ***\\\
# MULTIPLICATION TABLE MAKING
# ***///
# **//

num1=int(input("Enter Number for Reversed Order table = "))
mul_in_reverse=[x for x in range(1,11)]
mul_in_reverse.reverse()
for primary1 in mul_in_reverse: 
    with open("table in reverse order.txt","w") as a:
        for secondary1 in mul_in_reverse: 
            a.write(f"{num1} X {secondary1} = {num1*secondary1}")
            if secondary1 != 1:
                a.write("\n")

num2=int(input("Enter Number for Normal Order of table = "))
mul_in_normal=[y for y in range(1,11)]
for primary2 in mul_in_normal:
    with open("table in normal order.txt","w") as b:
        for secondary2 in mul_in_normal:
            b.write(f"{num2} X {secondary2} = {num2*secondary2}")
            if secondary2!=10:
                b.write("\n")
# *** \\\
# **    \\
# Code Ends \\
# **\\
# *** \\\                