c = 0 # count for palindromes
rev = 0
copy = 0

print("Palindromes b/w 100 and 200 :")
for i in range(100,201):
    rev = 0
    copy = i
    while (copy>0):
        rev = rev*10+(copy%10)
        copy=int(copy/10)
    # check for palindrome
    if (rev==i):
        print(i)
        c+=1
