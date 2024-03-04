from calcFunctions import addition, subtraction, sec_deg_formula, area_of_rectangle, area_of_square, area_of_circle

options: [str] = [
    "(1) Addition",
    "(2) Subtraction",
    "(3) 2nd Degree Formulas",
    "(4) Area of a Rectangle",
    "(5) Area of a Circle",
    "(6) Area of a Square"
]

# FUNCTIONS

def print_menu():

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

    elif user_input == "4":

        print("--Area of a Rectangle selected--\n")

        area_of_rectangle()

    elif user_input == "5":

        print("--Area of a Circle selected--\n")

        area_of_circle()

    elif user_input == "6":

        print("--Area of a Square selected--\n")

        area_of_square()

    else:
        print("Invalid Input")


# CODE EXECUTION


print("\nWelcome to PyCalc!\n")

while True:
    print_menu()

    user_input = input("Trykk ENTER for å bruke en annen formel."
                       "\n Skriv inn 'exit' for å avslutte programmet.\n")

    if user_input.lower() == "exit":
        break

    else:
        continue
