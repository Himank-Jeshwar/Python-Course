a=input("Enter Your Name=> ") 
b=input("Enter Your Age=> ")
print('''Dear''', a ,'''Welcome to COVID Checker''')

print('''Are you experiencing any symptoms of COVID-19:-
       Select from the options given below:-
       (1) Fever
       (2)Vomitting or Nausea
       (3)Cough or Cold
       (4)Loss of Smell and Taste
       (5)Headache
       (6)Difficulty in Breathing
       (7)Red eyes
       (8)Body ache 
       (9)None (Enter only numbers like 1 for Fever)''')
Others1=input("Others (optional) (Press Enter to Skip):- \n")

m={
    "1":"Okay...well so Take care ",
    "2":"Okay...well so Take care ",
    "3":"Okay...well so Take care ",
    "4":"Okay...well so Take care ",
    "5":"Okay...well so Take care ",
    "6":"Okay...well so Take care ",
    "7":"Okay...well so Take care ",
    "8":"Okay...well so Take care ",
    "9":"Good!That seems you have no symptoms of COVID-19",
    Others1:"Well According to what you said will be checked but take care"
 }


c=input("Enter the Problem Digit Here Below:-\n")
print(m.get(c)) 




print('''Do you have any of the diseases below:-
         (1)Diabetes
         (2)Cancer
         (3)Tuberculosis
         (4)Heart Problem
         (5)Glucoma
         (6)None ''')
Others2=input("Others (optional)(Press Enter to Skip) :-\n")
p={
    "1":'''Well it seems you have high risk of COVID-19
           It is recommend to stay at home and do not go out.
           Take Care...''',

    "2":'''Well it seems you have high risk of COVID-19
           It is recommend to stay at home and do not go out.
           Take Care...''',

    "3":'''Well it seems you have high risk of COVID-19
           It is recommend to stay at home and do not go out.
           Take Care...''',

    "4":'''Well it seems you have high risk of COVID-19
           It is recommend to stay at home and do not go out.
           Take Care...''',

    "5":'''Well it seems you have high risk of COVID-19
           It is recommend to stay at home and do not go out.
           Take Care...'''  ,

    "6":'''Your COVID infection risk is low but we recommend 
you to stay at home, wash your hands properly and wear a mask when you go outside'''  ,     

    Others2 :''' According to your problem it seems you have some risk of COVID-19
           It is recommend to stay at home and do not go out.
           Take Care...'''   
}      

d=input("Enter Disease Digit Below:-\n")
print(p.get(d))