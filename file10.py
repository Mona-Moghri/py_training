#assingment ==> write number and translate it word
number= input("phone: ")   #if we add int here we convert the whole num to int but we need it individually which can represent the key
convert={
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
words=[]
for i in number:
    if int(i) in convert:
        words.append(convert[int(i)])
print(" ".join(words)) #join method for receive combination of string


#mosh solution
'''number= input("phone: ")   #if we add int here we convert the whole num to int but we need it individually which can represent the key
convert={
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output= ""
for i in number:
    output += convert.get(i, "!") + " "   #get method when we type something beyond our dictionary it supply at the fault value
print(output)'''
