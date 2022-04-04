"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    display_menu = """ C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(display_menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_celsius(celsius)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_fahrenheit(fahrenheit)
        else:
            print("Invalid option")
        print(display_menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def convert_fahrenheit(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


main()
