x = 3 # Intial Value of "char"
rows = 9 # Number of rows
char="*" # Symbol
for i in range(rows): 
    if i<4:
        print(char*x)
        x+=1
    elif i<=8:
        print(char*x)
        x-=1    