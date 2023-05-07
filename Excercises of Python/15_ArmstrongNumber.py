n = int(input("Enter a number : "))
copy = n
s = 0
while(copy>0):
    s+=(copy%10)**3
    copy//=10

if (s==n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")