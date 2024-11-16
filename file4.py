#assignment: receive weight then convert it to the other unit
weight= int(input('how many kilos do you weight: '))   #i learn that i can write int behind the input instead of next line
convert= input("(L)bs or (K)g? ")
if convert.upper() == 'L':      #i didn't pay attention to upper method
    k = weight * 0.45    #solve this line with chatgpt
    print(f'you are {k} kilogram')
elif convert.upper() == 'K':
    l = weight * 2.20     #different way weight /0.45
    print(f'you are {l} pound')