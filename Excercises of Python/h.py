'''
           
  ||       ||     
  ||       ||
  ||       ||
  ||*******||
  ||       ||
  ||       ||
  ||       || 

'''
class LetterDesigner:
	def a(self):
		rows = 7
		spaces = 9
		inside_Space = 0
		spaceString = " "
		for a in range(rows):
			print(" "*spaces,end="")
			if a==0:
				print("/\\     ",end="")
			elif a==1:
				print(f"/{(spaceString*inside_Space)}\\     ",end="")	
			elif a==3 :
				print("/______\\     ",end="")
			elif a<7:
				print(f"/{spaceString*inside_Space}\\     ",end="")
			inside_Space+=2
			spaces-=1	
			print(" "*spaces)
	def h(self):
		rows = 7
		spaces = 2
		spaceString = " "
		star = "*"
		for i in range(rows):
			print(" "*spaces,end="")
			if i!=3:
				print(f"||{spaceString*(spaces+5)}||",end="")
		
			else :
				print(f"||{star*7}||",end="")
			print(" "*(spaces+8))
