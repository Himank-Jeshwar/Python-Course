'''
*
* #
* # *
* # * #
* # * # *
'''

for i in range(1,6):
    for j in range(0,i):
        if (j%2==0):
            print("* ",end="")
        else:
            print("# ",end="")
    print()
