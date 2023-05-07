lottery={
 1:" You have won Bottle x2",
 2:"You have won Table Fan",
 3:"You have won TV",
 4:"You have won Bag x1",
 5:"You have won Harry Potter Book",
 6:"You have won Mobile Phone",
 7:"You have won Laptop",
 8:"You have won Fridge" ,
 9:"You have won Bike",
 10:"You have won Car",
}
print("Select any of the numbers below :-\n",lottery.keys()) 
num=int(input("Enter the Number = "))
print(lottery.get(num))  