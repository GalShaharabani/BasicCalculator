from math import *


class Calculator:

    def __init__(self, num1, num2, actions):
        self.actions = actions["+", "-", "*", "/", "s", "^", "c", "r"]
        self.num1 = num1
        self.num2 = num2

    def load_actions(self):
        return ["+", "-", "*", "/", "s", "^", "c", "r"]

    def add(number1, number2):
        print("Result: ")
        print(float(number1) + float(number2))
        return float(number1) + float(number2)

    def subtract(number1, number2):
        print("Result: ")
        print(float(number1) - float(number2))
        return float(number1) - float(number2)

    def multiply(number1, number2):
        print("Result: ")
        print(float(number1) * float(number2))
        return float(number1) * float(number2)

    def divide(number1, number2):
        print("Result: ")
        print(float(number1) / float(number2))
        return float(number1) / float(number2)

    def square_root(number1):
        print("Result: ")
        print(float(sqrt(number1)))
        return sqrt(number1)

    def power(number1, number2):
        print("Result: ")
        print(float(number1) ** float(number2))
        return float(number1) ** float(number2)

    def clear(number1, number2):
        number1 = 0
        number2 = 0
        result = number1 + number2
        print(result)
        return result

    # def redo(number2):
    #     num2 = 0
    #     return num2


