A = [x for x in range(1,11)]
print("A =",A)

n = len(A)

for i in range(0,n//2):
    temp = A[i]
    A[i] = A[n-i-1]
    A[n-i-1] = temp

print("A =",A)