from math import *


class Calculator:
    actions=["+", "-", "*", "/", "s", "^", "c", "r"]
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def load_actions(self, actions):
        return actions

    def add(self, number1, number2):
        print("Result: ")
        print(float(number1) + float(number2))
        return float(number1) + float(number2)

    def subtract(self, number1, number2):
        print("Result: ")
        print(float(number1) - float(number2))
        return float(number1) - float(number2)

    def multiply(self, number1, number2):
        print("Result: ")
        print(float(number1) * float(number2))
        return float(number1) * float(number2)

    def divide(self, number1, number2):
        print("Result: ")
        print(float(number1) / float(number2))
        return float(number1) / float(number2)

    def square_root(self, number1):
        print("Result: ")
        print(float(sqrt(number1)))
        return sqrt(number1)

    def power(self, number1, number2):
        print("Result: ")
        print(float(number1) ** float(number2))
        return float(number1) ** float(number2)

    def clear(self, number1, number2):
        self.number1=0
        self.number2=0
        print(number1+number2)
        return number1+number2

    # def repeat(number1, number2, action):
    #     actions = Calculator.actions
    #     last_action = None
    #     for action in  actions:
    #         last_action = action
    #     if last_action == actions[0]:
    #         Calculator.add(number1, number2)
    #     elif action == actions[1]:
    #         Calculator.subtract(number1, number2)
    #     elif action == actions[2]:
    #         Calculator.multiply(number1, number2)
    #     elif action == actions[3]:
    #         Calculator.divide(number1, number2)
    #     elif action == actions[4]:
    #         Calculator.square_root(number1)
    #     elif action == actions[5]:
    #         Calculator.power(number1, number2)
    #     elif action == actions[6]:
    #         Calculator.clear(number1, number2)
    # def redo(number2):
    #     num2 = 0
    #     return num2


