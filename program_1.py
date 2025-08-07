# Small calculator which performs operations such as Addition, Subtraction, Multiplication, and Division using a class.

class Calculator:
    def __init__(self, a: float, b: float):
        """
        Constructor to initialize two numbers.
        :param a: First number (float)
        :param b: Second number (float)
        """
        self.a = a
        self.b = b

    def calculate(self, operation: str):
        """
        Performs the given arithmetic operation on the two numbers.
        :param operation: Type of operation (add, subtract, multiply, divide)
        :return: Result of the operation
        """
        try:
            if operation == 'add':
                return self.a + self.b
            elif operation == 'subtract':
                return self.a - self.b
            elif operation == 'multiply':
                return self.a * self.b
            elif operation == 'divide':
                if self.b != 0:
                    return self.a / self.b
                else:
                    return "Error: Division by zero"
        except Exception as e:
            return f"Unexpected error occurred: {str(e)}"

# List of valid operations
valid_operations = ['add', 'subtract', 'multiply', 'divide']

# Function to get valid float input from user
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to get valid operation input from user
def get_valid_operation():
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide): ").lower()
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation! Please enter one of: add, subtract, multiply, divide.")

# Main program logic
def main():
    print("=== Simple Calculator ===")
    a = get_valid_float("Enter first number: ")
    b = get_valid_float("Enter second number: ")
    operation = get_valid_operation()

    calc = Calculator(a, b)
    result = calc.calculate(operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
