letter='''
                                       Address:-<|City|>,<|State|>
                                       Date:-<|Date|>

               Dear <|Name|>,
                I am writing this letter to tell you.
                Due to increasing cases around our area of Covid-19.
                I recommend you to stay home.If by any chance you want to go out,
                wear double masks,carry a hand sanitizer and maintain social-distancing.

                 \t\tSTAY HOME,STAY SAFE! 

                Your Loving Friend,
                <|sender|>'''

name=input("Enter The Name=\n")
city=input("Enter Your City=\n")
state=input("Enter Your State=\n")
sender=input("Enter The Sender's Name\n")
date=input("Enter The Date=\n")
letter=(letter.replace("<|Name|>",name))
letter=(letter.replace("<|Date|>",date))
letter=(letter.replace("<|sender|>",sender)) 
letter=(letter.replace("<|City|>",city))
letter=(letter.replace("<|State|>",state))
print(letter) 