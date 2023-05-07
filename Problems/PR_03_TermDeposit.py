class TermDeposit:
    sumofmoney=0.0
    days=0
    def takeInput(self):
        TermDeposit.sumofmoney = float(input("Enter the sum of money : "))
        TermDeposit.days = int(input("Enter number of days : "))
    
    def display(self):
        amt = 0.0
        if (TermDeposit.days<=180):
            amt = TermDeposit.sumofmoney+(TermDeposit.sumofmoney*5.5/100)
        elif(TermDeposit.days<=364):
            amt = TermDeposit.sumofmoney+(TermDeposit.sumofmoney*7.5/100)
        elif(TermDeposit.days==365):
            amt = TermDeposit.sumofmoney+(TermDeposit.sumofmoney*9.0/100)
        else: 
            amt = TermDeposit.sumofmoney+(TermDeposit.sumofmoney*8.5/100)

        print("Maturity Amount = Rs. ",amt)

deposit = TermDeposit()
deposit.takeInput()
deposit.display()