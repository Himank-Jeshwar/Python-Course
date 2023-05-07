mul=[1,2,3,4,5,6,7,8,9,10]
mul.reverse()
for a in range(2,26):
    with open(f"Multiplication table of {a}","w") as m:   
        for i in mul:
            m.write((f"{a} X {i} = {a*i}"))
            if i!=1:
                m.write("\n")        