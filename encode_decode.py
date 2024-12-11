# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#other way to call the file
#import art
#print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

# TODO-2: What happens if the user enters a number/symbol/space?


    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""

        if encode_or_decode == "decode":  # if statement outside because the shift direction affects all letters in the message. Changing shift_amount should only happen once at the start, not for each letter.
            shift_amount *= -1

        for letter in original_text:
            if letter in alphabet:   # if statement inside because each letter might be different (a letter or a space or a symbol) and needs a specific processing rule.

                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]

            else:
                output_text += letter

        print(f"Here is the {encode_or_decode}d result: {output_text}")


    # TODO-3: Can you figure out a way to restart the cipher program?

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    choose_continue= input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if choose_continue != "yes":
        print("Goodbye")
        break