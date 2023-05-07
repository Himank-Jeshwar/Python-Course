numbers=[1,7,12,11,22]       
even=[i for i in numbers if i%2==0]
print(even) 

s1={9,5,23,12,34,34}
odd={o for o in s1 if o%2==1}
print(odd)

p=[9,9,9,12,13,45,45,67,54,54]
s2={items for items in p}
print(s2)

op=[9,12,34,23,10,78,2,3,1,4,5,6]
l=[k for k in op if k<8]
print(l)