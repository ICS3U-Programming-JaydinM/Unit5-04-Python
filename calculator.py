#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-12-14
# This program is a calculator but it only always two numbers


def Calculator(num1, num2, operation):

    # Match case statement structure used for each possible operation
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2
        case _:
            return -1


def main():
    # Gets the users two numbers
    num1_str = input("Enter a number: ")

    num2_str = input("Enter a second number: ")

    # Tries casting the numbers to float
    try:
        user_num1 = float(num1_str)
        user_num2 = float(num2_str)
    # Tells the user it did not enter two number then ends the program
    except:
        print("You Need to enter 2 numbers.")
    # displays all the Operations they can use
    else:
        print("\nall the Operation sign you can to use: +, -, *, /, %")

        # Gets the operation from the user
        operation_user = input("Enter an operation: ")

        # Storing return value inside the result variable
        result = Calculator(user_num1, user_num2, operation_user)

        # If the user enters invalid data for the  operator Choice
        if result == -1:
            print(f"\n{operation_user} is not a valid operation.")

        else:
            # Displays the answer of the calculation to the user
            print(f"\n{user_num1} {operation_user} {user_num2} = {result}")


if __name__ == "__main__":
    main()
