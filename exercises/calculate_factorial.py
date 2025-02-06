# implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial_recursive(number - 1)


def main():
    # handle negative input
    try:
        print("Factorial Computation Using Recursion")
        number = int(input("Enter a non-negative integer: "))

        while number < 0:
            number = int(input("Must enter a non-negative integer. Please re-enter: "))

        factorial = factorial_recursive(number)
        print("The factorial of " + str(number) + " is: " + str(factorial))
    # Call factorial_recursive method
    except ValueError:
        print("Invalid input. Non integer value entered.")

if __name__ == "__main__":
    main()
