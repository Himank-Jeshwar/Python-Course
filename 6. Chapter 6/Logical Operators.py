age1=int(input("Enter Your Age=\n"))
if (age1>=18 and age1<=30): #(Both the conditions must be true)
    print("You are eligible")
else:
    print("You are not eligible") 

age2=int(input("Enter Your Age=\n"))
if (age2>=18 or age2<=30): #(Either Condition1 or Condition2 must be true)
    print("You are eligible")
else:
    print("You are not eligible") 

age3=int(input("Enter Your Age=\n"))
if (not age3>=18 ): #(it means if age not equal or greater than 18 print "You are eligible" else "You are not eligible"    
    print("You are eligible")
else:
    print("You are not eligible") 

