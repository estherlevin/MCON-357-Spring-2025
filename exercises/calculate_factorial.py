import sys
# implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial_recursive(number - 1)

#iterative factorial method
def factorial_iterative(number):
    result = 1
    for i in range(1, number + 1):  #start from 1 to include all numbers up to 'number'
        result *= i
    return result

# getting integer from user
def process_input(input_str):
    error_message = ""
    value = None
    try:
        value = int(input_str)
        if value < 0:
            #if value is negative, return None plus error message
            return None, "Number must be a positive integer."
        return value, error_message
    except ValueError as e:
        error_message = "Number must be a positive integer."
        return None, error_message

def main():
    print("Factorial Computation Using Recursion")

    while True:
        input_str = input("Enter non-negative integer: ")
        value, error_message = process_input(input_str)
        if value is not None and error_message == "":
            try:
                factorial = factorial_recursive(value)
                print(f"The factorial of {value} is: {factorial}")
            except RecursionError:
                print("Recursive limit exceeded. Switching to iterative calculation.")
                factorial = factorial_iterative(value)
                print(f"The factorial of {value} is: {factorial}")
            exit(0)
        else:
            print(error_message)
            continue

if __name__ == "__main__":
    main()
