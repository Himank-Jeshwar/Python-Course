# AUTHOR - HIMANK JESHWAR
# DATE - 10/8/21

# This program prints the cube root of the numbers in the list.
# This list made by list comprehension.
# This list is same as the below :-
#(l1=[1,8,27,64,125,216,343,512,729,1000,1331,1728,2197,2744,3375,4096,4913,5832,6859,8000])
num=[(x**3) for x in range(1,21)]
for c in num:
    print(f"Cube Root of {c} = {c**(1/3)}")