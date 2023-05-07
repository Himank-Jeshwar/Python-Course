# AUTHOR - HIMANK JESHWAR
# WRITTEN ON - 03/11/2021

'''
Question :-
    Make this Figure in Python Using For-Loop
         
		  *
         * * 
        *   *
       *     *
      *       *
     *         *
    *           *
   ***************
               
'''
rows = 8 # Number of rows in the figure."
char = 1 # Initial Value of "char."
n = 1  # Initial Value of "n".
space=" "
for z in range(rows): 
	# 			     ''' MAIN CODE '''
	
	print(space*(9-z+1) ,end="") # Space on the left side of the figure.
	if z==0:
		print(f"*"*char ,end="") # This is the tip of the figure.	
	elif z==7 :
		print(f"*"*(char+7) ,end="") # This is the last part of the figure.
	else:
		print(f"*{space*(n-2)}*" ,end="") # This part lies between the tip and the last part of the figure.
	
	print(space*(9-z+1)) # Space given on the right side of the figure.
	char+=1 
	n+=2  

		#		**/Code Ends/**