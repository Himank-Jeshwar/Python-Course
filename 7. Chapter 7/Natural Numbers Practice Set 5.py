n=int(input("Enter the first n natural numbers = "))
natural=0    
while n>0:
    natural+=n
    n-=1
print(f"The sum is {natural}.")  