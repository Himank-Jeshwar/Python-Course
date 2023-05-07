def music(music):
    return ("Select from the options below :-",music.items()) 

song={
    1: "Breatha- josh pan",
    2:"June",
    3:"Meet & Fun Ofshane!"
}
print(music(song))
s=int(input("Enter Music Number \n Like (1 for Breatha- josh pan)= "))

if s==1:
    from playsound import playsound
    playsound("C:\\Users\\Himank Jeshwar\\Videos\\Breatha - josh pan.mp3")

elif s==2:
    from playsound import playsound
    playsound("C:\\Users\\Himank Jeshwar\\Videos\\Video Songs\\June.wav")

elif s==3:
    from playsound import playsound
    playsound("C:\\Users\\Himank Jeshwar\\Videos\\Meet & Fun! - Ofshane.mp3")    


else:
    print("No song of this type available.")