def remove_strip(s,word):
    new=s.replace(word,"") #Removes the word by placing a space instead of it.
    return new.strip() 
name="          Himank Is A Good Boy          " 
print(remove_strip(name,"Boy"))        
# print(name.strip())   # strip() ignore the wide spaces   