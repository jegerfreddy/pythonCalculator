from calcFunctions import addition, subtraction, sec_deg_formula

options: [str] = [
    "(1) Addition",
    "(2) Subtraction",
    "(3) 2nd Degree Formulas"
]


def print_menu():
    print("\nWelcome to PyCalc!\n")

    for option in options:
        print(option)

    user_input = input("Choose an option: ")

    result: int = 0

    if user_input == "1":

        print("--Addition selected--\n")

        addition()

    elif user_input == "2":

        print("--Subtraction selected--\n")

        subtraction()

    elif user_input == "3":

        print("--2nd Degree Formula selected--\n")

        sec_deg_formula()

    else:
        print("Invalid Input")


print_menu()