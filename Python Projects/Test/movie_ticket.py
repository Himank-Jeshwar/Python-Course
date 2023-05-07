import time
print('''\t\t\t       Movie Booking Center
\t\t\t      ======================''')
# Work From Ticket Selling Authorities
class Movie_Counter :
    m1 = 46
    m2 = 150 
    m3 = 30 
    m4 = 20 
    m5 = 10
    def __init__(self,shows):
        self.shows=shows 
    def availableShows(self):
        # Shows Available Seats
            print(f'''                      {self.shows[0]} : 11 a.m  (Seats Available = {Movie_Counter.m1})
                      {self.shows[1]} : 12:30 p.m (Seats Available = {Movie_Counter.m2})
                      {self.shows[2]} : 1:30 p.m (Seats Available = {Movie_Counter.m3})
                      {self.shows[3]} : 2:40 p.m (Seats Available = {Movie_Counter.m4})
                      {self.shows[4]} : 12:00 a.m (Seats Available = {Movie_Counter.m5})''')
    def giveTicket(self,showName):
        '''This Function gives the ticket to the customer.'''
        # showName is editable put any movie name.
        if showName == "Chehre" :
            nameOfShow = "movie1"
        elif showName == "The Guilty":
            nameOfShow = "movie2"
        elif showName == "Godzilla V/S Kong":
            nameOfShow = "movie3" 
        elif showName == "The Dark Knight":
            nameOfShow = "movie4"
        elif showName == "The Conjuring 3":
            nameOfShow = "movie5"               
        
        # Takes number of seats to book
        seatNo=int(input("\t\tEnter the number of seats to book = "))

        '''If the user asks for more seats and the number is more then the
        available seats then the user is said to decrease the "seatNo" 
        or he won't be able to book the ticket '''

        if seatNo>Movie_Counter.m1 and nameOfShow == "movie1" and Movie_Counter.m1!=0 :
            print(f"{seatNo-Movie_Counter.m1} more seat(s) are not available. Try again with less number of seats.")
        elif seatNo>Movie_Counter.m2 and nameOfShow == "movie2" and Movie_Counter.m2!=0 :
            print(f"{seatNo-Movie_Counter.m2} more seat(s) are not available. Try again with less number of seats.")
        elif seatNo>Movie_Counter.m3 and nameOfShow == "movie3" and Movie_Counter.m3!=0 :
            print(f"{seatNo-Movie_Counter.m3} more seat(s) are not available. Try again with less number of seats.")
        elif seatNo>Movie_Counter.m4 and nameOfShow == "movie4" and Movie_Counter.m4!=0 :
            print(f"{seatNo-Movie_Counter.m4} more seat(s) are not available. Try again with less number of seats.")    
        elif seatNo>Movie_Counter.m5 and nameOfShow == "movie5" and Movie_Counter.m5!=0 :
            print(f"{seatNo-Movie_Counter.m5} more seat(s) are not available. Try again with less number of seats.")
        
        ''' This is to book the ticket if the number of seats asked for booking
        is less than or equal to the available seats '''
        if showName in self.shows:
            if seatNo <= Movie_Counter.m1 and nameOfShow == "movie1"  :
                print(f'''\n
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    Name of the show = {showName}               
                                    Time of the show =  11:30 a.m                      
                                    Number of Seats Booked = {seatNo}                         
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
            elif seatNo <= Movie_Counter.m2 and nameOfShow == "movie2" :
                print(f'''\n
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    Name of the show = {showName}               
                                    Time of the show =  11:30 a.m                      
                                    Number of Seats Booked = {seatNo}                         
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
            elif seatNo <= Movie_Counter.m3 and nameOfShow == "movie3" :
                print(f'''\n
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    Name of the show = {showName}               
                                    Time of the show =  11:30 a.m                      
                                    Number of Seats Booked = {seatNo}                         
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
            elif seatNo <= Movie_Counter.m4 and nameOfShow == "movie4" :
                print(f'''\n
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    Name of the show = {showName}               
                                    Time of the show =  11:30 a.m                      
                                    Number of Seats Booked = {seatNo}                         
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
            elif seatNo <= Movie_Counter.m5 and nameOfShow == "movie5" :
                print(f'''\n
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    Name of the show = {showName}               
                                    Time of the show =  11:30 a.m                      
                                    Number of Seats Booked = {seatNo}                         
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
        else :
            print(f"The show '{showName}' is currently not available.")                

        
        # If showName is there in the list then only book the tickets
        if showName in self.shows:
            if nameOfShow == "movie1":
                Movie_Counter.m1-=seatNo    
            elif nameOfShow == "movie2":
                Movie_Counter.m2-=seatNo
            elif nameOfShow == "movie3":
                Movie_Counter.m3-=seatNo
            elif nameOfShow == "movie4":
                Movie_Counter.m4-=seatNo
            elif nameOfShow == "movie5":
                Movie_Counter.m5-=seatNo   

        # If all tickets are sold , show "Housefull"
        if Movie_Counter.m1<0 :
                print("\n\tHousefull ! Try for this in different time slot.")
        elif Movie_Counter.m2<0 :
            print("\n\tHousefull ! Try for this in different time slot.")    
        elif Movie_Counter.m3<0 :
                print("\n\tHousefull ! Try for this in different time slot.")            
        elif Movie_Counter.m4<0 :
                print("\n\tHousefull ! Try for this in different time slot.")   
        elif Movie_Counter.m5<0 :
                print("\n\tHousefull ! Try for this in different time slot.")
       
        # Don't show negative values , so I wrote this            
        if Movie_Counter.m1<0:
            Movie_Counter.m1=0
        elif Movie_Counter.m2<0:
            Movie_Counter.m2=0
        elif Movie_Counter.m3<0:
            Movie_Counter.m3=0
        elif Movie_Counter.m4<0:
            Movie_Counter.m4=0
        elif Movie_Counter.m5<0:
            Movie_Counter.m5=0            
    
    def takeTicket (self,showName):
        # THIS FUNCTION TAKES TICKET IF USER CANCEL THE TICKET
        seatNo=int(input("\t\tEnter the number of seats to cancel = "))

        # showName can be changed (editable)    
        if showName == "Chehre" :
                nameOfShow = "movie1"
        elif showName == "The Guilty":
                nameOfShow = "movie2"
        elif showName == "Godzilla V/S Kong":
                nameOfShow = "movie3" 
        elif showName == "The Dark Knight":
                nameOfShow = "movie4"
        elif showName == "The Conjuring 3":
                nameOfShow = "movie5"
    

        # Numbers such as the 46,150 and so on are been taken because these are the seats which are initially took.
        # If seats are cancelled , add it to the available seats.
        if showName in self.shows:
            if nameOfShow == "movie1" and 46>(Movie_Counter.m1+seatNo):
                print(f"                      The Ticket for the show '{showName}' has been cancelled.\n                      Note: NO MONEY WILL BE REFUNDED. \n")  
                Movie_Counter.m1+=seatNo    
            elif nameOfShow == "movie2" and 150>(Movie_Counter.m2+seatNo):
                print(f"                      The Ticket for the show '{showName}' has been cancelled.\n                      Note: NO MONEY WILL BE REFUNDED. \n")  
                Movie_Counter.m2+=seatNo 
            elif nameOfShow == "movie3"and 30>(Movie_Counter.m3+seatNo):
                print(f"                      The Ticket for the show '{showName}' has been cancelled.\n                      Note: NO MONEY WILL BE REFUNDED. \n")  
                Movie_Counter.m3+=seatNo
            elif nameOfShow == "movie4"and 20>(Movie_Counter.m4+seatNo):
                print(f"                      The Ticket for the show '{showName}' has been cancelled.\n                      Note: NO MONEY WILL BE REFUNDED. \n")  
                Movie_Counter.m4+=seatNo
            elif nameOfShow == "movie5"and 10>(Movie_Counter.m5+seatNo):
                print(f"                      The Ticket for the show '{showName}' has been cancelled.\n                      Note: NO MONEY WILL BE REFUNDED. \n")  
                Movie_Counter.m5+=seatNo   
            else :
                print("\tDear User ,\n\t   It seems like you haven't booked a ticket yet , So we are unable to cancel your ticket. ")
        
        # If showName is not there show this
        else :
            print("\n\t\tYou can't cancel this ticket as this show is not there .")        

class Ticket_Buyer :
    def bookTicket(self): # This function takes the name of the show to book
        nameForBook=input("\n\t\tEnter the name of the show to book = ")
        return nameForBook
    def cancelTicket(self):# This function takes the name of the show to cancel   
        nameForCancel=input("\n\t\tEnter the name of the show to cancel= ")
        return nameForCancel

movies=Movie_Counter([f"Chehre","The Guilty","Godzilla V/S Kong","The Dark Knight","The Conjuring 3"])
buyer=Ticket_Buyer()

# Main Menu for the user to perform any action
while True:
    print('''         \t       =====================================
                       = Press 1 to See Available Tickets  =
                       = Press 2 to Book Tickets           =
                       = Press 3 to Cancel Tickets         =
                       = Press 4 to exit                   =
                       =====================================''')               
    choice=int(input("\n\t\tEnter Your Choice = "))  

    # Assigning tasks to each buttons
    if choice == 1:
        movies.availableShows() 
    elif choice == 2:
        movies.giveTicket(buyer.bookTicket()) 
        '''buyer.bookTicket() is the parameter of movies.giveticket()
        which takes name from the user to book Ticket.'''                                        
    elif choice == 3:
        movies.takeTicket(buyer.cancelTicket()) 
        '''buyer.cancelTicket() is the parameter of movies.takeTicket()
        which takes name from the user to cancel Ticket.'''
    elif choice == 4:
        print("\t\tHope You Enjoyed,\n\t\tThanks for Visiting !")
        time.sleep(1) # Creating a 1 sec pause after the message is printed and then program is exited.
        exit()