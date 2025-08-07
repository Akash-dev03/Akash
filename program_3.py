# Problem-3:
# Given a single integer 'a', generate a series of odd numbers
# based on the pattern where every 2 values of 'a' increase
# the number of odd numbers printed by 2 (e.g., 1 → 1, 3 → 3, 5 → 5, etc.)

try:
    # Ask user for input
    a = int(input("Enter a number (a): "))

    # Handle negative input
    if a < 0:
        print("Error: Please enter a non-negative integer.")

    # Handle case when a == 0
    elif a == 0:
        print("No numbers to display. Please enter a value greater than 0.")

    else:
        # Calculate number of odd values based on input pattern
        count = (a // 2) * 2 + 1  # ensures 1 → 1, 3 → 3, 5 → 5, etc.

        # Generate 'count' number of odd values: 1, 3, 5, ...
        output = [2 * i + 1 for i in range(count)]

        # Print the output
        print("Odd number series:")
        print(", ".join(map(str, output)))

except ValueError:
    # Handle case where input is not an integer
    print("Error: Please enter a valid integer.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Unexpected error occurred: {str(e)}")
