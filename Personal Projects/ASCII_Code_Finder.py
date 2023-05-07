smallAlphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capitalAlphabets = [x.upper() for x in smallAlphabets]
def asciiForCaps(letter):
    smallAlphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    capitalAlphabets = [x.upper() for x in smallAlphabets]
    asciiValuesForCapital = [i for i in range(65,91)]
    if letter!=letter.lower():
        if letter in capitalAlphabets:
                indexOfLetter = capitalAlphabets.index(letter)
        asc = asciiValuesForCapital[indexOfLetter]
        return asc       
    else:
        return "INVALID ARGUMENT : Must be a capital letter."

def asciiForSmall(letter):
    smallAlphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    asciiValuesForSmall = [ x for x in range(97,123)]
    if letter!=letter.upper():
        if letter in smallAlphabets:
                indexOfLetter = smallAlphabets.index(letter)
        asc = asciiValuesForSmall[indexOfLetter]
        return asc       
    else:
        return "INVALID ARGUMENT : Must be a small letter."

def findLetter(asc):
    smallAlphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    capitalAlphabets = [x.upper() for x in smallAlphabets]
    asciiValuesForCapital = [i for i in range(65,91)]
    asciiValuesForSmall = [ x for x in range(97,123)]
    letter=""
    if asc>=65 and asc<=90:
        if asc in asciiValuesForCapital:
            indexValue = asciiValuesForCapital.index(asc)
            letter = capitalAlphabets[indexValue]
    elif asc>=97 and asc<=122:
        if asc in asciiValuesForSmall:
            indexValue = asciiValuesForSmall.index(asc)
            letter = smallAlphabets[indexValue]
    else :
        return "INVALID ARGUMENT : invalid ASCII value for alphabet."
    return letter

def findNumber(asc):
    numberList = [i for i in range(0,10)]
    ascii_values = [a for a in range(48,58)]
    if asc>=48 and asc<=57:
        number = numberList[ascii_values.index(asc)]
    else:
        return "INVALID ARGUMENT : invalid ASCII value for number."
    return number        

def findSymbol(asc):
    symbolList1 = [" ","!","\"","#","$","%","&","\'","(",")","*","+",",","-",".","/"]
    symbolList2 = [":",";","<","=",">","?","@"]
    symbolList3 = ["[","\\","]","^","_","`"]
    symbolList4 = ["{","|","}","~"]
    ascii_values1 = [a1 for a1 in range(32,48)]
    ascii_values2 = [a2 for a2 in range(58,65)]
    ascii_values3 = [a3 for a3 in range(91,97)]
    ascii_values4 = [a4 for a4 in range(123,127)]
    if (asc>=32 and asc<=47):
        symbol = symbolList1[ascii_values1.index(asc)]
    elif (asc>=58 and asc<=64):
        symbol = symbolList2[ascii_values2.index(asc)]
    elif (asc>=91 and asc<=96):
        symbol = symbolList3[ascii_values3.index(asc)]
    elif (asc>=123 and asc<=126):
        symbol = symbolList4[ascii_values4.index(asc)]
    else :
        return "INVALID ARGUMENT : invalid ASCII value for symbol."
    return symbol

def ascii_of_number(num):
    if (num>=0 and num<=9):
        ascii_values = [i for i in range(48,58)]
        numList = [x for x in range(0,10)]
        asc = ascii_values[numList.index(num)]
    else:
        return "INVALID ARGUMENT : out of range , should be within [0-9]."
    return asc

def ascii_of_symbol(symbol):
    symbolList1 = [" ","!","\"","#","$","%","&","\'","(",")","*","+",",","-",".","/"]
    symbolList2 = [":",";","<","=",">","?","@"]
    symbolList3 = ["[","\\","]","^","_","`"]
    symbolList4 = ["{","|","}","~"]
    ascii_values1 = [a1 for a1 in range(32,48)]
    ascii_values2 = [a2 for a2 in range(58,65)]
    ascii_values3 = [a3 for a3 in range(91,97)]
    ascii_values4 = [a4 for a4 in range(123,127)]
    if symbol in symbolList1:
        asc = ascii_values1[symbolList1.index(symbol)]
        return asc
    elif symbol in symbolList2:
        asc = ascii_values2[symbolList2.index(symbol)]
        return asc
    elif symbol in symbolList3:
        asc = ascii_values3[symbolList3.index(symbol)]
        return asc
    elif symbol in symbolList4:
        asc = ascii_values4[symbolList4.index(symbol)]
        return asc
    else:
        return "INVALID ARGUMENT : not a symbol."
    
# print(ascii_of_symbol("#"))