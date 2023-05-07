def division(num1,num2):
    try:
        return int(num1)/int(num2)
    except:
        raise ZeroDivisionError (f"Division By Zero (DIV/o)")
div=division("20","0")
print(div)