c = 0 # count for primes
factors = 0
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

if (n1<0):
    n1*=-1
if (n2<0):
    n2*=-1

m = min(n1,n2)
n = max(n1,n2)

print("Primes b/w",m,"and",n,":")
for i in range(n,m+1,-1):
    factors = 0
    for j in range(2,i):
        if (i%j==0):
            factors+=1

    if (factors!=0):
        continue

    c+=1
    print(i)
