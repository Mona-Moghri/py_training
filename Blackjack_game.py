# my attempt for solving problem. 
# in this task i learn which i have problem to use functoin, 
# i mean where should i use it, and how can i use it properlly
import random
from traceback import print_tb

import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    start_game = input("Do you want to play a game of blackjack ? Type 'y' or 'n': ").lower()
    print(art.logo)
    while start_game == "y":
        user_cards= random.sample(cards, 2)
        computer_cards= random.sample(cards,2)
        sum_user_cards= sum(user_cards)
        sum_computer_card= sum(computer_cards)

        print(f"   your cards: {user_cards}, current score: {sum_user_cards}")
        print(f"   computer's first card: {computer_cards[0]}")

        if computer_cards == 21:
            print("user lose")
            return
        elif sum_user_cards == 21:
            print("user win")
            return


        while sum_user_cards < 21:
            user_continue_playing = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_continue_playing == "y":
                new_user_card = random.choice(cards)
                user_cards.append(new_user_card)
                sum_user_cards = sum(user_cards)
                if 11 in user_cards and sum_user_cards > 21:
                    user_cards = [1 if card == 11 else card for card in user_cards]
                    sum_user_cards = sum(user_cards)
                print(f"   your cards: {user_cards}, current score: {sum_user_cards}")
                print(f"   computer's first card: {computer_cards[0]}")

            elif user_continue_playing == "n":
                break

        if sum_user_cards > 21:
            print(f"   computer's final hand: {computer_cards}, final score: {sum_computer_card}")
            print("You went over. you lose")

        while sum_computer_card < 17:
            new_computer_card = random.choice(cards)
            computer_cards.append(new_computer_card)
            sum_computer_card= sum(computer_cards)

            if sum_computer_card > 21 or sum_user_cards > sum_computer_card:
                print("user win")
            elif sum_user_cards < sum_computer_card:
                print("you lose")
            else:
                print("draw")
        start_game = input("Do you want to play again? type 'y' or 'n': ").lower()
        if start_game == "y":
            print("\n" * 20)
            print(art.logo)


deal_card()


#this is the course solution:
# def deal_card():
#     """Returns a random card from the deck"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card


# def calculate_score(cards):
#     """Take a list of cards and return the score calculated from the cards"""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0

#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)

#     return sum(cards)


# def compare(u_score, c_score):
#     """Compares the user score u_score against the computer score c_score."""
#     if u_score == c_score:
#         return "Draw 🙃"
#     elif c_score == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif u_score == 0:
#         return "Win with a Blackjack 😎"
#     elif u_score > 21:
#         return "You went over. You lose 😭"
#     elif c_score > 21:
#         return "Opponent went over. You win 😁"
#     elif u_score > c_score:
#         return "You win 😃"
#     else:
#         return "You lose 😤"


# def play_game():
#     print(logo)
#     user_cards = []
#     computer_cards = []
#     computer_score = -1
#     user_score = -1
#     is_game_over = False

#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())

#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards: {user_cards}, current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))


# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     print("\n" * 20)
#     play_game()