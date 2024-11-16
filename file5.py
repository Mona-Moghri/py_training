# guess number assingment, solve it with the help of gpt
x=9
attempt=0   #gpt which represent the number of guess that user have made
while attempt < 3 and attempt != x:
    guess = int(input('guess: '))
    attempt +=1
    if attempt == 3:    #gpt suggest to use if
        print('sorry you failed')
    elif guess == x:
        print('you are win')
#Mosh way for this assingment
'''secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input('guess: '))
    guess_count +=1
    if secret_number == guess:
        print('you won!')
        break
else:
    print('sorry you failed')'''