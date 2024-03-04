import math
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


def area_of_rectangle():
    while True:
        length: float = float(input("Definer lengden L: "))
        width: float = float(input("Definer bredden B: "))

        print(f"\nArealet til et rektangel med verdiene:\n"
              f"L = {length}\n"
              f"B = {width}\n\n"
              f"Areal = {length * width}\n")

        break


def area_of_square():
    while True:
        side: float = float(input("Definer en side S: "))

        print(f"\nArealet til et kvadrat med verdien:\n"
              f"S = {side}\n\n"
              f"Areal = {side * side}\n")

        break


def area_of_circle():
    while True:
        radius: float = float(input("Definer radius r: "))

        print(f"\nArealet til et rektangel med verdiene:\n"
              f"r = {radius}\n\n"
              f"Areal = {math.pi * radius**2}\n")

        break
