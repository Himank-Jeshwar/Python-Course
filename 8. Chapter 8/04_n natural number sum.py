num=int(input("Enter Number of Natural Numbers = "))
def total(n):
    if n==0 or n<=0:
        return "Not a natural number"
    else:
        return n*(n+1)/2 
print(f"The sum of {num} natural numbers is {total(num)}.") 