def factorial_iter(num):
    product=1
    for a in range(num):
        product=product*(a+1)
    return product


def factorial_recursive(num):
    if num==1 or num==0 :
        return 1
    return num*factorial_recursive(num-1)

# print(factorial_iter(4))
print(factorial_recursive(4))      