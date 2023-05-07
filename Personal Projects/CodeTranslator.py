import ASCII_Code_Finder
class Converter:
    def __init__(self,code):
        self.code = code
    def decimalToBinary(self):
        try: 
            int(self.code)
            if self.code==0:
                return "0000"
            elif self.code==1:
                return "0001"
            else:
                tempString = ""
                n = self.code

                while (n!=0):
                    o = n
                    rem = o%2
                    n=int(n/2)
                    tempString+=str(rem)
                
                length = len(tempString)
                binary=""
                for i in range (length-1,-1,-1):
                    binary+=tempString[i]
                return binary
        except ValueError:
            return "INVALID ARGUMENT : Not a decimal value"
        except TypeError:
            return "INVALID ARGUMENT : Not a decimal value"   

    def binaryToDecimal(self):
        length = len(self.code)
        isBinary = True
        for i in range(0,length):
            if self.code[i]!="0" and self.code[i]!="1":
                isBinary=False    
                
        if isBinary==True:
            decimal = 0
            for i in range(0,length):
                decimal+=int(self.code[i])*(2**(length-i-1))
            return decimal
        elif isBinary==False:
            return "INVALID ARGUMENT : Not a Binary Digit."


    def decimalToOctal(self):
        tempString = ""
        n = self.code
        while(n!=0):
            o = n
            rem = o%8
            n = int(n/8)
            tempString+=str(rem)
        length = len(tempString)
        octal = ""
        for i in range(length-1,-1,-1):
            octal+=tempString[i]
        return octal

    def octalToDecimal(self):
        decimal = 0
        strOctal = str(self.code)
        length = len(strOctal)
        if self.code%10!=8:
            for i in range(0,length):
                decimal+=int(strOctal[i])*(8**(length-i-1))
            return decimal
        else:
            return ("INVALID ARGUMENT : Not an Octal Number.")

    

    def decimalTohex(self):
        hexLetters = ["A","B","C","D","E","F"]
        hexNumbers = [10,11,12,13,14,15]
        tempString = ""
        n = self.code
        while (n!=0):
            o = n
            rem = o%16
            n = int(n/16)
            if rem>9:
                tempString+=hexLetters[hexNumbers.index(rem)]
            else :
                tempString+=str(rem)
        length = len(tempString)
        hexadecimal = ""
        for i in range(length-1,-1,-1):
            hexadecimal+=tempString[i]
        return hexadecimal

    def hexToDecimal(self):
        self.code=self.code.upper()
        otherLetters = ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        # verifying whether the given argument is hexadecimal or not
        isHex = True
        for other in otherLetters:
            if other in self.code:
                isHex = False 

        if isHex == True :
            decimal = 0
            hexNumbers = [10,11,12,13,14,15]
            hexLetters = ["A","B","C","D","E","F"]
            length = len(self.code)

            for z in range(0,length):
                if self.code[z] in hexLetters:
                    val=hexNumbers[hexLetters.index(self.code[z])]
                    decimal+=val*16**(length-z-1)
                else:
                    decimal+=int(self.code[z])*16**(length-z-1)
            return decimal
        return "INVALID Argument : Not a hexadecimal number."

    def textToBinary(self):
        binary=""
        for letter in self.code:
            binaryLetters=""
            tempString=""
            if letter==" ":
                binaryLetters="100000"
                binaryLetters+=" "
                binary+=binaryLetters
            else:
                try:
                    letter = int(letter)
                    asc = ASCII_Code_Finder.ascii_of_number(letter)
                except ValueError:
                    if letter==letter.lower() in ASCII_Code_Finder.smallAlphabets:
                        asc = ASCII_Code_Finder.asciiForSmall(letter)
                    elif letter==letter.upper() in ASCII_Code_Finder.capitalAlphabets :
                        asc = ASCII_Code_Finder.asciiForCaps(letter)
                    else:
                        asc = ASCII_Code_Finder.ascii_of_symbol(letter)
                n = asc
                while (n!=0):
                    o = n
                    rem = o%2
                    n = int(n/2)
                    tempString+=str(rem)
                for i in range(len(tempString)-1,-1,-1):
                    binaryLetters+=tempString[i]
                binaryLetters+=" "
                binary+=binaryLetters
        return binary


    def binaryToText(self):
        # verifying whether the given argument is binary or not
        isBinary = True
        for i in range(0,len(self.code)):
            if self.code[i]!="0" and self.code[i]!="1": 
                isBinary = False
        # if it is binary , program will proceed or it will execute the else block 
        if isBinary==True:
            text=""
            splitedWords = self.code.split() 
            for words in splitedWords:
                asc=0
                for i in range(0,len(words)):
                    letter=""
                    asc+=int(words[i])*2**(len(words)-i-1)
                    if (asc>=65 and asc<=90) or (asc>=97 and asc<=122):
                        letter = ASCII_Code_Finder.findLetter(asc)
                    elif (asc>=32 and asc<=47) or (asc>=58 and asc<=64) or (asc>=91 and asc<=96) or (asc>=123 and asc<=126):
                        letter = ASCII_Code_Finder.findSymbol(asc)
                    elif (asc>=48 and asc<=57):
                        letter = str(ASCII_Code_Finder.findNumber(asc))
                text+=letter
            return text
        else:
            return "INVALID ARGUMENT : Not a binary value."

