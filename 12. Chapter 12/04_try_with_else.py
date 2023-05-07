try:
    i=int(input("Enter a Number = "))
    c=2/i
except Exception as e:
    print(e) 
    print("Operation Failed!")
else:
    print("Operation Succeeded!")       