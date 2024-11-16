#assignment (car game) ==> use gpt for some section
start= False
stop= False
attempt=0
command=input('>').lower()
while command != 'quit':
    if command == 'help':
        print('start - to start the car \nstop - to stop the car \nquit - to exit')
    elif command == 'start':
        if not start:
            print ('car started...ready to go!')
            start = True
        else:
            print('car is already start')
    elif command == 'stop':
        if not stop:
            print('car stopped')
            stop = True
        else:
            print('car is already stop')
    else:
        print("i don't understand that")
    attempt+=1
    command = input('>').lower()