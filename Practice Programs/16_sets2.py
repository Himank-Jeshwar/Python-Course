# A = {34,12,56,78,90,33,41,67}
# B = {90,12,78,99,100,121,96,34,150,161}

# Find :
# i) n(A)  ii)n(B) iii) n(A-B) iv) n(B-A) v) n(AUB) vi) n(AnB)
def n(givenSet):
    cardinalNo = 0
    for i in givenSet:
        cardinalNo+=1
    return cardinalNo
A = {34,12,56,78,90,33,41,67}
B = {90,12,78,99,100,121,96,34,150,161}
OnlyA = n(A)-n(A.intersection(B))
OnlyB = n(A.union(B))-n(A)
print("Cardinal No of A =",n(A))
print("Cardinal No of B =",n(B))
print("Cardinal No of A-B =",n(A-B))
print("Cardinal No of B-A =",n(B-A))
print("Cardinal No of AUB =",n(A.union(B)))
print("Cardinal No of A-B =",n(A.intersection(B)))

print("No.of subsets in A =",2**n(A),"; Proper Subsets of A =",2**n(A)-1)
print("No.of subsets in B =",2**n(B),"; Proper Subsets of B =",2**n(B)-1)