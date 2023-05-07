import os
with open("Making html.txt") as code:
    html=code.read()
with open("Making html.html","w") as code:
    file=code.write(html) 
os.remove("Making html.txt") 