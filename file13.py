#create rock, papre and scissor game:

#for starting the code it is really important to breaking down the logic of the project before start


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice= [rock, paper, scissors]
choose_your_item= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choose= random.randint(0,2)
if 2< choose_your_item < 0:  #first we should check the validation of number
    print("you choose wrong number. you loose")
else:
    print(choice[choose_your_item])
    print("computer choose")
    print(choice[computer_choose]) #we have input which 0,1,2 which act like index to access a specific item in the list
    if choose_your_item == computer_choose:
        print("it is a draw!")
    elif (choose_your_item == 0 and computer_choose == 2) or \
        (choose_your_item == 1 and computer_choose == 0) or \
        (choose_your_item == 2 and computer_choose == 1):    #use \ for able to enter and write the rest of the code on new line
        print("you win!")
    else:
        print("you lose")


