logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


first_input = int(input("Enter the first number: "))

while True:
    operator_selection = input("\n +\n -\n *\n /\n Pick an operation: \n")
    second_input = int(input("Enter the second number: "))

    if operator_selection == "+":
        result = add(first_input, second_input)
        print(result)
    elif operator_selection == "-":
        result = sub(first_input, second_input)
        print(result)
    elif operator_selection == "*":
        result = mul(first_input, second_input)
        print(result)
    elif operator_selection == "/":
        result = div(first_input, second_input)
        print(result)
    else:
        print("Select the correct operation")
        continue

    while True:
        continue_calculation = input("Continue working with the previous result (yes or no): ").lower()
        if continue_calculation == "yes":
            first_input = result
            break
        elif continue_calculation == "no":
            first_input = int(input("Enter the first number: "))
            break
        else:
            print("Please enter 'yes' or 'no': ")
