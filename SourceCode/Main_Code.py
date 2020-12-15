import os
import re

reserved_words = ['if','then','else','repeat','until','end','read','write']
special_symbols = ['=', '<', '<=', '>', '>=', ':=', '+', '-', '*', '/', ';', '==', '!=']
Characters= "[a-zA-z_$][a-zA-Z_0-9$]*"

def FindTokens(InputText,Tokens):
    TokensFound=re.findall(Tokens,InputText)
    return TokensFound
def IsIdentifier(Token):
    # function to check if token is identifier by checking that it is formed from characters and not a reserved words
    global Characters
    regexp =re.compile(Characters)

    if (regexp.search(Token)) and (Token not in reserved_words):
        return True
    return False

filename = "input.txt"
filePath = os.path.abspath(filename)
mode = "rt"
openFile = open(filePath,mode)
myFileText = openFile.read()
openFile.close()

# Removing the comments between {}
inputWithoutComments = re.sub(r'{.*}', '', myFileText)
# Removing Blank Lines
inputWithoutComments_andWithoutNewLines = inputWithoutComments.strip('\n')

symbolsRegExp = '(\:=|\*|\+|\-|\;|\(|\)|\/|\>=|\!=|\==|\=|\>|\<=|\<' # added open bracket in the start of the str
charactersRegExp= '|[a-zA-z_$][a-zA-Z_0-9$]*|' # added 2 OR operators
NumbersRegExp='[0-9]+[[\.][0-9]+]?|[0-9]+)'  # added closed bracket
GeneralRegExp=symbolsRegExp+charactersRegExp+NumbersRegExp

TokensFound=FindTokens(inputWithoutComments,GeneralRegExp)

outputDict= {}

for token in TokensFound:
    if token in reserved_words:
        outputDict[token] = "Reserved Word"
    elif token in special_symbols:
        outputDict[token] = "Special Symbol"
    elif IsIdentifier(token):
        outputDict[token] = "Identifier"
    else:
        outputDict[token] = "Number"



for key,value in outputDict.items():
    print(key,":",value,"\n")

output=open("output.txt","wt")
for key,value in outputDict.items():
    output.write(str(key)+":"+str(value)+"\n"+"\n")
output.close()

