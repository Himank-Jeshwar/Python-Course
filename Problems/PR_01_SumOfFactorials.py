factorial = 1
sumofFactorials = 0

for i in range(4,11):
    factorial = 1
    for j in range(1,i+1):
        factorial*=i
    print(i,"!=",factorial)
    sumofFactorials+=factorial

print("Sum of factorials =",sumofFactorials)