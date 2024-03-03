from math import sqrt


def addition():
    while True:

        a: str = input("Enter first number: ")
        b: str = input("Enter second number: ")

        if int(a) and int(b):
            print(f"Resultatet er: {int(a) + int(b)}")
            break

        else:
            continue


def subtraction():
    while True:

        a: str = input("Enter first number: ")
        b: str = input("Enter second number: ")

        if int(a) and int(b):
            print(f"Resultatet er: {int(a) - int(b)}")
            break

        else:
            continue


def sec_deg_formula():
    while True:

        a: float = float(input("Definer A: "))

        if float(a) == 0:
            print("[OBS!] A kan ikke defineres som 0 i en andregradsligning.")
            continue

        b: float = float(input("Definer B: "))
        c: float = float(input("Definer C: "))

        discriminant: float = (b**2-4*a*c)

        if discriminant < 0:
            print(f"\nEn andregradsligning hvor...\nA = {a}\nB = {b}\nC = {c}\n"
                  f"har ingen løsning fordi deskriminanten (b**2 - 4*a*c) er < 0")
            break

        x1: float = (-b - sqrt(discriminant)) / (2*a)
        x2: float = (-b + sqrt(discriminant)) / (2*a)

        print(f"\nx1 = {x1} \nx2 = {x2}")

        break
