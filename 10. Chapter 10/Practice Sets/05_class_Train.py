class Train:
    def __init__(self,train_name,fare,seats):
        self.train_name=train_name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print(f"Name of Train = {self.train_name}")
        print(f"Seats Available = {self.seats}")
          
    def getFare(self):
        print(f"Fare of the Ticket = Rs. {self.fare}")  
     
    def bookTicket(self):    
        if self.seats>0:
            print("Ticket Booked.") 
            print(f"Your Seat number is {self.seats} at Coach No. B12")  
            self.seats=self.seats-1
        else:
            print("Ticket Not Available For this Train !\n") 
    def cancelTicket(self,seatNo):
        self.seatNo=seatNo
        print(f"The ticket for seat number {seatNo} is cancelled.")
        self.seats=self.seats+1
        print(f"Seat Number {self.seatNo} is vacant now.")

intercity = Train("RajDhani Express",1450,8)
intercity.getStatus()
print("\n")
intercity.bookTicket()
print("\n")
intercity.cancelTicket(8)
intercity.getStatus()