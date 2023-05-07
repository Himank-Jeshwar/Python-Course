from functools import reduce
import time
class BasicCal:
    '''Basic Calculator class - Does basic operations like addition, substraction, 
    division, multiplication.'''
    def add(n1,n2):
        '''Returns the sum of given arguments.'''
        return n1+n2
    def sub(n1,n2):
        '''Returns the substraction of given arguments.'''
        return n1-n2
    def mul(n1,n2):
        '''Returns the product of given arguments.'''
        return n1*n2
    def div(dividend,divisor):
        '''Divides the dividend by divisor and returns the answer.'''
        return dividend/divisor
class AdvancedCal:
    '''Advanced Calculator class - Does advanced operations like finding square, cube, 
    square root and cube root.'''
    def sq(n):
        '''Returns square of the given argument. '''
        return n**2
    def cube(n):
        '''Returns cube of the given argument. '''
        return n**3
    def cbrt(n):
        '''Returns cube root of the given argument. '''
        return n**(1/3)
    def sqrt(n):
        '''Returns square root of the given argument. '''
        return n**(0.5)
    def power(n,p):
        '''Returns first argument raised to the power of second argument.'''    
        return n**p
def gcd(n1,n2):
    '''Greatest Common Divisor (GCD) or Highest Common Factor (HCF) is 
    the largest integer that can divide the numbers without a remainder.
    
    This function returns the GCD of given arguments.'''
    if n2==0:
        return n1
    return int(gcd(n2,n1%n2))
def lcm(n1,n2):
    '''Least Common Multiple (LCM) is the smallest positive integer that is
    the multiple of all the given numbers.
    
    This functions returns the LCM of given arguments.'''
    return int((n1*n2)/gcd(n2,n1%n2))

if __name__ == "__main__":
    while True:
        print(
            '''
                        ====================================================== 
                        =                BASIC OPERATIONS                    =
                        =                ==================                  =
                        =                 Press + for addition               =
                        =                 Press - for substraction           = 
                        =                 Press * for multiplication         =
                        =                 Press / for division               = 
                        =                                                    =
                        =                 ADVANCED OPERATIONS                =
                        =                =====================               =
                        =        Press s to find square of a number          =
                        =        Press c to find cube of a number            =
                        =        Press w to find square root of a number     =
                        =        Press z to find cube root of a number       =
                        =                                                    =
                        =               GCD & LCM Calculations               =
                        =             =========================              =
                        =        Press g to find GCD of given numbers        =
                        =        Press l to find LCM of given numbers        = 
                        =                                                    =
                        =              BUTTON FOR EXIT                       = 
                        =             =================                      =
                        =              Press e to EXIT                       =
                        ======================================================
        ''')
        try:
            op = input("Enter Your Choice = ")
            op = op.lower()
            if op == '/':
                dividend = float(input("Enter value for dividend = "))
                divisor = float(input("Enter value for divisor = "))
                print("Answer = ",BasicCal.div(dividend,divisor))
                
            elif op == '+':
                n = 1
                numbers = []
                while n<=15:
                    if n%10==1 and n!=11:
                        num = input(f"Enter {n}st number =  ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break
        
                    elif n%10==2 and n!=12:
                        num = input(f"Enter {n}nd number =  ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break                       
                    elif n%10==3 and n!=13:
                        num = input(f"Enter {n}rd number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break    
                    else :
                        num = input(f"Enter {n}th number (Press ENTER to skip)=  ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break
                    n+=1
        
                print("\nAnswer = ",reduce(BasicCal.add,numbers))
                
            elif op == '-':
                n = 1
                numbers = []
                while n<=15:
                    if n%10==1 and n!=11:
                        num = input(f"Enter {n}st number = ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break    
                    elif n%10==2 and n!=12:
                        num = input(f"Enter {n}nd number =  ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break     
                    elif n%10==3 and n!=13:
                        num = input(f"Enter {n}rd number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break    
                    else :
                        num = input(f"Enter {n}th number (Press ENTER to skip) = ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break
                    n+=1
                print("\nAnswer = ",reduce(BasicCal.sub,numbers))

            elif op == '*':
                n = 1
                numbers = []
                while n<=15:
                    if n%10==1 and n!=11:
                        num = input(f"Enter {n}st number = ") 
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break
                    elif n%10==2 and n!=12:
                        num = input(f"Enter {n}nd number = ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break                        
                    elif n%10==3 and n!=13:
                        num = input(f"Enter {n}rd number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break    
                    else :
                        num = input(f"Enter {n}th number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(float(num))
                        elif num=="":
                            break
                    n+=1
                print("\nAnswer = ",reduce(BasicCal.mul,numbers))

            elif op == "s":
                num = input("Enter Number to find Square = ")
                if num=="":
                    print("Cannot be blank here !\nTry Again.")
                else:
                    print(f"\nAnswer = ",AdvancedCal.sq(float(num)))

            elif op == "c":
                num = input("Enter Number to find Cube = ")
                if num=="":
                    print("Cannot be blank here !\nTry Again.")
                else:
                    print(f"\nAnswer = ",AdvancedCal.cube(float(num)))

            elif op == "w":
                num = input("Enter Number to find Square Root = ")
                if num=="":
                    print("Cannot be blank here !\nTry Again.")
                else:
                    print(f"\nAnswer = ",AdvancedCal.sqrt(float(num)))
        
            elif op == "z":
                num = input("Enter Number to find Cube Root = ")
                if num=="":
                    print("Cannot be blank here !\nTry Again.")
                else:
                    print(f"\nAnswer = ",AdvancedCal.cbrt(float(num)))

            elif op == "g":
                n = 1
                numbers = []
                while n<=15:
                    if n%10==1 and n!=11:
                        num = input(f"Enter {n}st number =  ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break    
                    elif n%10==2 and n!=12:
                        num = input(f"Enter {n}nd number =  ")
                        if num!="":
                            numbers.append(int(num)) 
                        elif num=="":
                            break     
                    elif n%10==3 and n!=13:
                        num = input(f"Enter {n}rd number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break    
                    else :
                        num = input(f"Enter {n}th number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break
                    n+=1
                print("\nAnswer = ",reduce(gcd,numbers))

            elif op == "g":
                n = 1
                numbers = []
                while n<=15:
                    if n%10==1 and n!=11:
                        num = input(f"Enter {n}st number = ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break   
                    elif n%10==2 and n!=12:
                        num = input(f"Enter {n}nd number = ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break  
                    elif n%10==3 and n!=13:
                        num = input(f"Enter {n}rd number (Press ENTER to skip) = ") 
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break    
                    else :
                        num = input(f"Enter {n}th number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break
                    n+=1
                print("\nAnswer = ",reduce(gcd,numbers))
                
            elif op == "l":
                n = 1
                numbers = []
                while n<=15:
                    if n%10==1 and n!=11:
                        num = input(f"Enter {n}st number =  ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break 
                    elif n%10==2 and n!=12:
                        num = input(f"Enter {n}nd number =  ")
                        if num!="":
                            numbers.append(int(num))     
                    elif n%10==3 and n!=13:
                        num = input(f"Enter {n}rd number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break    
                    else :
                        num = input(f"Enter {n}th number (Press ENTER to skip) =  ")
                        if num!="":
                            numbers.append(int(num))
                        elif num=="":
                            break
                    n+=1
                print("\nAnswer = ",reduce(lcm,numbers))
            elif op=='e':
                print('''Hope You Enjoyed !
                        Thanks for using this calculator !''')
                time.sleep(1)       
                exit()
            else :
                print ("INVALID INPUT !\nPlease Try Again.")    
        except TypeError :
            print ("FIRST FIELD CANNOT BE BLANK !")
        except ValueError :
            print ("CANNOT BE BLANK HERE!")