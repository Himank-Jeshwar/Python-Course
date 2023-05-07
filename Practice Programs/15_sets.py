# UniversalSet = {x:x belongs to N , x<=30}
# A = {"factors of 45"} 
# B = {"multiples of 5"}

# find these
# i) A U B  ii) A n B  iii) A-B  iv) B-A  v) A' vi) B'
UniversalSet = {x for x in range(1,61)}
A = {y for y in UniversalSet if 45%y==0} # => {1,3,5,9,15,45}
B = {t for t in UniversalSet if t%5==0} # => {5,10,15,20,25,30,35,40,45,50,55,60}
AUB = A.union(B)
AnB = A.intersection(B)
OnlyA = A-B  # elements of A which are not in B 
OnlyB = B-A # elements of B which are not in A
ComplementOfA = UniversalSet-A # not A
ComplementOfB = UniversalSet-B # not B
print(AUB) # => {1, 3, 5, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60}
print(AnB) # => {45, 5, 15}
print(OnlyA) # {1,3,9}
print(OnlyB) # {35, 40, 10, 50, 20, 55, 25, 60, 30}


print("A' =",ComplementOfA)
print("B' =",ComplementOfB)