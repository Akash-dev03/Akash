def count_divisibles(numbers, max_divisor=9): 
    """
    Count how many numbers in the list are divisible by each number from 1 to max_divisor.

    Parameters:
        numbers (list): List of integers to check.
        max_divisor (int): Maximum divisor to check against (inclusive).

    Returns:
        dict: A dictionary with divisors as keys and counts as values.
    """
    if not numbers:
        raise ValueError("Input list is empty.")

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    
    if not isinstance(max_divisor, int) or max_divisor < 1:
        raise ValueError("max_divisor must be a positive integer greater than or equal to 1.")

    result = {}
    for i in range(1, max_divisor + 1):
        result[i] = sum(1 for num in numbers if num % i == 0)
    
    return result


# Main program
try:
    # Prompt user to input numbers separated by commas
    user_input = input("Enter a list of integers separated by commas (e.g., 1,2,3): ").strip()

    if not user_input:
        raise ValueError("No input provided.")

    # Convert input string to list of integers
    numbers = [int(x.strip()) for x in user_input.split(",")]

    # Call the function to compute divisibility counts
    result = count_divisibles(numbers)

    # Print results
    print("\nDivisibility Count:")
    for divisor, count in result.items():
        print(f"{divisor}: {count}")

except ValueError as e:
    print(f"Input Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
