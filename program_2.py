# Problem-2:
# Given a single integer 'a', generate the first 'a' odd numbers starting from 1.
# Examples:
#   Input: a = 1 → Output: 1
#   Input: a = 2 → Output: 1, 3
#   Input: a = 3 → Output: 1, 3, 5
#   Input: a = 4 → Output: 1, 3, 5, 7

try:
    # Prompt the user for input
    a = int(input("Enter a number (a): "))

    # Validate that input is non-negative
    if a < 0:
        print("Error: Please enter a non-negative integer.")
    elif a == 0:
        # Handle the case when user enters 0
        print("No numbers to display. Please enter a value greater than 0.")
    else:
        # Generate first 'a' odd numbers: 1, 3, 5, 7, ...
        odd_numbers = [2 * i + 1 for i in range(a)]

        # Print the result in comma-separated format
        print("Odd number series:")
        print(", ".join(map(str, odd_numbers)))

except ValueError:
    # Handle case where input is not an integer
    print("Error: Please enter a valid integer.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Unexpected error occurred: {str(e)}")