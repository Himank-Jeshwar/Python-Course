try:
    def total(a,b):
       
        if __name__=="__main__":
            a=int(input("Enter first number = "))
            b=int(input("Enter second number = "))
        ans=a+b    
        return ans
except:
    raise ValueError (f"string is given instead of int()")    