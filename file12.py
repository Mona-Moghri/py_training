#important information that i learnt is using the chart for starting my code which i like map and me to have vision of the process
#game treasure
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choos_your_way= input("choose left or right? L or R: ").lower()
if choos_your_way == "l":
    choosehow= input("wait for boat or swim: ").lower()
    if choosehow == "wait":
        door= input("which door? Red, Yellow, Blue").lower()  #we can use \ before simbel which means don't check this simble
        if door == "yellow":
            print("You Win")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over")
        elif door == "red":
            print("Burned by fire.\nGame Over")
    else:
        print("Attacked by trout\nGame Over")
else:
    print("Fall into a holw.\nGame Over")