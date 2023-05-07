# num= 1x2x3x4x...num (This only means factorial.)
num=int(input("Enter Any Number = "))
factorial=1
for a in range(1, num+1):
    factorial=factorial*a
print(f"The factorial of {num} is {factorial}.")     