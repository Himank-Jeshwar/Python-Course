'''
                    *
                   ***
                  *****   
                 *******      
                *********       
               ***********
                *********
                 *******   
                  *****
	           ***
                    *
'''
x = 1
rows = 11
spaces = 20
for i in range(rows):
	if i<5:
		print(" "*spaces,end="")
		print("*"*x,end="")
		print(" "*spaces)
		x+=2
		spaces-=1
	elif i<=10:
		print(" "*spaces,end="")
		print("*"*x,end="")
		print(" "*spaces)
		x-=2
		spaces+=1
	                    