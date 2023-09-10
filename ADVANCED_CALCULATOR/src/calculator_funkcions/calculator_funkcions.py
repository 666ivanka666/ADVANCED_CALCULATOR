from src.utils.calculation_action import (
    action_multiply, action_subtract, action_add,
    action_divide, action_sine, action_cosine,
    action_tangent, action_square, action_square_root, action_root, 
    action_exponent, action_logarithm
)
from src.db.model.calculator import run_app2
from src.db.model.calculator import MemoryCalculator


def run_app():
    calculator = MemoryCalculator()
    while True:
        action = input("1 - Multiply, 2 - Subtract, 3 - Add, 4 - Divide, 5 - Sine, 6 - Cosine, 7 - Tangent, 8 - Square, 9 - n-Square, 10 - n-Root, 11- n-Exponent, 12- Log,  q - Quit: ")

        try:
            if action == "1":
                calculator.store_in_memory(action_multiply())

            elif action == "2":
                calculator.store_in_memory(action_subtract())

            elif action == "3":
                calculator.store_in_memory(action_add())

            elif action == "4":
                calculator.store_in_memory(action_divide())

            elif action == "5":
                calculator.store_in_memory(action_sine())

            elif action == "6":
                calculator.store_in_memory(action_cosine())

            elif action == "7":
                calculator.store_in_memory(action_tangent())

            elif action == "8":
                calculator.store_in_memory(action_square())

            elif action == "9":
                calculator.store_in_memory(action_square_root())

            elif action == "10":
                calculator.store_in_memory(action_root())

            elif action == "11":
                calculator.store_in_memory(action_exponent())

            elif action == "12":
                calculator.store_in_memory(action_logarithm())

            elif action.lower() == "q":
                break

            else:
                print("Invalid action. Please try again.")

        except Exception as e:
            print("An error occurred:", str(e))

        run_app2(calculator)
