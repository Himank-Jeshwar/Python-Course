num=int(input("Enter Number to check whether its prime or not = "))
for a in range(2, num):
    if num%a==0:
        print(num,"is not a prime number")
        break
else:    
    print(num,"is a prime number") 