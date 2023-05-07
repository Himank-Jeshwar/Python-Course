n=3
row = 3
for d in range(row):
    print(" " * (n-d-1), end="")
    print("*" * (2*d+1), end="")
    print(" " * (n-d-1))

