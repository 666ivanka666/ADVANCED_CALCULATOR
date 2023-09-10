from src.calculator_funkcions.calculator_funkcions import (
    action_multiply, action_subtract, action_add,
    action_divide, action_sine, action_cosine,
    action_tangent, action_square, action_square_root,
    action_root, action_exponent, action_logarithm
)

class MemoryCalculator:
    def __init__(self):
        self.memory = None

    def use_memory(self):
        return self.memory

    def store_in_memory(self, value):
        print(f"Value is: {value}")
        if value is not None:
            self.memory = value
            print(f"Value {self.memory} stored in memory.")
        else:
            print("Unable to store value in memory.")


    def clear_memory(self):
        self.memory = None
        print("Memory cleared.")

    def perform_operation_with_memory(self, operation):
        if self.memory is not None:
            try:
                if operation == "1":
                    num_of_numbers = int(input("Enter the number of numbers: "))
                    result = self.memory  # Initialize result with memory value
                    for _ in range(num_of_numbers):
                        num = float(input("Enter a number: "))
                        result = action_multiply(result, num)
                elif operation == "2":
                    num = float(input("Enter a number to subtract: "))
                    result = action_subtract(self.memory, num)
                elif operation == "3":
                    num = float(input("Enter a number to add: "))
                    result = action_add(self.memory, num)
                elif operation == "4":
                    num = float(input("Enter a number to divide: "))
                    result = action_divide(self.memory, num)
                elif operation == "5":
                    result = action_sine(self.memory)
                elif operation == "6":
                    result = action_cosine(self.memory)
                elif operation == "7":
                    result = action_tangent(self.memory)
                elif operation == "8":
                    result = action_square(self.memory)
                elif operation == "9":
                    result = action_square_root(self.memory)
                elif operation == "10":
                    num = float(input("Enter a number to root: "))
                    result = action_root(self.memory, num)
                elif operation == "11":
                    num = float(input("Enter a number to exponent: "))
                    result = action_exponent(self.memory, num)
                elif operation == "12":
                    num = float(input("Enter the base number: "))
                    result = action_logarithm(self.memory, num)
                else:
                    print("Invalid operation.")
                    return

                print(f"The result of the operation is: {result}")
                self.store_in_memory(result)  # Store the result in memory
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return
        else:
            print("Memory is empty.")

    def calculate(self, operation):
        if self.memory is not None:
            try:
                if operation == "1":
                    num = float(input("Enter a number to multiply: "))
                    result = action_multiply()
                elif operation == "2":
                    num = float(input("Enter a number to subtract: "))
                    result = action_subtract()
                elif operation == "3":
                    num = float(input("Enter a number to add: "))
                    result = action_add()
                elif operation == "4":
                    num = float(input("Enter a number to divide: "))
                    result = action_divide()
                elif operation == "5":
                    result = action_sine()
                elif operation == "6":
                    result = action_cosine()
                elif operation == "7":
                    result = action_tangent()
                elif operation == "8":
                    result = action_square()
                elif operation == "9":
                    result = action_square_root()
                elif operation == "10":
                    num = float(input("Enter a number to root: "))
                    result = action_root()
                elif operation == "11":
                    num = float(input("Enter a number to exponent: "))
                    result = action_exponent()
                elif operation == "12":
                    num = float(input("Enter a number to logarithm: "))
                    result = action_logarithm()
                else:
                    print("Invalid operation.")
                    return

                print(f"The result of the operation is: {result}")
                self.store_in_memory(result)  # Store the result in memory
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Memory is empty.")

def run_app2(calculator):
    while True:
        try:
            action = input("1 - Store in memory, 2 - Recall from memory, 3 - Clear memory, 4 - Perform operation with memory, q - Quit: ")

            if action == "1":
                num = float(input("Enter a number: "))
                calculator.store_in_memory(num)

            elif action == "2":
                value = calculator.use_memory()
                if value is not None:
                    print(f"The value in memory is: {value}")
                else:
                    print("Memory is empty.")

            elif action == "3":
                calculator.clear_memory()

            # elif action == "4":
            #     operation = input("Enter an operation (1 - Multiply, 2 - Subtract, 3 - Add, 4 - Divide, 5 - Sine, 6 - Cosine, 7 - Tangent, 8 - Square, 9 - n-Square, 10 - n-Root, 11- n-Exponent, 12- Log, q- Quit): ")
            #     calculator.calculate(operation)
            
            elif action == "4":
                if calculator.memory is None:
                    print("No value stored in memory. Please perform a calculation and store a value in memory first.")
                else:
                    num = float(input("Enter a number to perform the operation with: "))
                    operation = input("Enter an operation (1 - Multiply, 2 - Subtract, 3 - Add, 4 - Divide, 5 - Sine, 6 - Cosine, 7 - Tangent, 8 - Square, 9 - n-Square, 10 - n-Root, 11- n-Exponent, 12- Log): ")

                    if operation == "1":
                        result = calculator.memory * num
                    elif operation == "2":
                        result = calculator.memory - num
                    elif operation == "3":
                        result = calculator.memory + num
                    elif operation == "4":
                        if num == 0:
                            print("Cannot divide by zero.")
                            continue
                        result = calculator.memory / num
                    
                    elif operation == "5":
                        result = calculator.sine(calculator.memory)
                    elif operation == "6":
                        result = calculator.cosine(calculator.memory)
                    elif operation == "7":
                        result = calculator.tangent(calculator.memory)
                    elif operation == "8":
                        result = calculator.square(calculator.memory)
                    elif operation == "9":
                        result = calculator.n_square(calculator.memory)
                    elif operation == "10":
                        result = calculator.n_root(calculator.memory)
                    elif operation == "11":
                        result = calculator.n_exponent(calculator.memory)
                    elif operation == "12":
                        result = calculator.logarithm(calculator.memory)
                    else:
                        print("Invalid operation.")
                        continue

                    calculator.store_in_memory(result)
                    print("Result:", result)


            elif action.lower() == "q":
                break

            else:
                print("Invalid action. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

