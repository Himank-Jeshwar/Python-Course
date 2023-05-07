def printPattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print((2*j+1),end=" ")
        print()

def printSeries(n):
    k = 11
    s = 0
    for i in range(1,n+1):
        print((i*i),end="/")
        print(k,end=" ")
        s+=(i*i/k)
        k+=10

    print("\nSum =",s)

ch = int(input("Enter choice : "))
n = int(input("Enter value for n : "))

if (ch==1):
    printSeries(n)

elif (ch==2):
    printPattern(n)
else:
    print("INVALID INPUT !")
