sub1=int(input("Enter the Marks of Maths=  "))
sub2=int(input("Enter the Marks of English=  "))
sub3=int(input("Enter the Marks of Computer=  "))
total_sub=sub1+sub2+sub3

if(sub1<33 or sub2<33 or sub3<33):
    print("Fail in one subject!As you got less than 33 percent in one of the subject")
elif total_sub/3 <40:
    print("Fail,as you got less than total percentage that is 40%")
else:
    print("Congratulations! You have passed.")    