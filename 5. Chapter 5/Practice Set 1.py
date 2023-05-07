dic1={
    "Imaandar":"Honest",
    "Bhasha":"Language",
    "Kaalpanik":"Imagination",
    "Asambhav":"Impossible"
}
print("Select any word Below to know the meaning:=",dic1.keys())
a=input("Enter the Hindi Word=\n")
print("The translated English word is=\n",dic1.get(a)) 