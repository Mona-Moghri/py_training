import art
print(art.logo)


def outer_function(previous_result=None):    #By setting previous_result=None, we make the parameter optional
    if previous_result is None:
        first_number= float(input("What's the first number?: "))
        print("+", "-", "*", "/", sep="\n") #if we need to have output horizontally
    else:
        first_number = previous_result
    mathematical_option= input("Pick an operation: ")
    second_number= float(input("What's the next number?: "))

    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    #don't need () in front of functions in dictionary because we try to store them not use them
    operations= {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if mathematical_option in operations:
        previous_result= operations[mathematical_option](first_number,second_number)
        print(f"the result is:{first_number} {mathematical_option} {second_number} = {previous_result}")

    continue_operatoin = input("Type 'y' to continue calculating with 0.0, or type 'n' to start a new calculat: ").lower()
    if continue_operatoin == "y":
        outer_function(previous_result)
    elif continue_operatoin == "n":
        print("\n" * 20)
        print(art.logo)
        outer_function()
outer_function()
