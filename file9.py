#solve this assignment with inner loop that contain nested loop which appear F shape on output
numbers= [5, 2, 5, 2, 2]
for num in numbers:
    for _ in range(num):   #(_) is just a placeholder because we don’t need the actual number inside this loop
        print('*', end='')    #end='' means not move to the next line
    print()   #for moving to the next line
#mosh solution -- i need to have better concept of this piece of code
'''numbers= [5, 2, 5, 2, 2]
for x_count in numbers:
    output= ''  #represent the store characters which will be added in the next step
    for count in range(x_count):
        output +='x'
    print(output)'''