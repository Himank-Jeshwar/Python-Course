n = int(input("Enter a number :"))
rev = int(0)
while(n>0):
    rev = rev*10+(n%10)
    n=int(n/10)
print(rev)