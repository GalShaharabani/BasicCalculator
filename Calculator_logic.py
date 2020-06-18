from math import *


# CALCULATIONS
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


actions = ["+", "-", "*", "/", "s", "^", "c", "r"]
#           0    1    2    3    4    5    6    7
print("Welcome!")
num1 = float(input("enter first number: "))
num2 = 0
action = input("action: ")
valid_action=True

if action == actions[4]:
    num2 =0

while len(action) != 1:
    valid_action=False
    print("invalid action")
    action = input("enter a valid action: ")
    if len(action) == 1:
        valid_action=True

if valid_action and action != actions[4]:
    num2 = float(input("enter second number: "))


def calculate(number1, op, number2):
    n1 = number1
    n2 = number2
    act = op
    while act != actions[0] and act != actions[1] and act != actions[2] and act != actions[3] \
            and act != actions[4] and act != actions[5] and act != actions[6] and act != actions[7]:
        print(str(act) + " is not an action")
        act = input("enter a valid action: ")
        n2 = float(input("enter another number: "))
    # for act in actions:
    #     i=0
    #     if act != actions[i]:
    #         print(str(act) + " is not an action")
    #         act = input("enter a valid action: ")
    #         n2 = float(input("enter another number: "))
    #     i+=1

    while True:

        if act == actions[0]:
            n1 = add(n1, n2)
            result = n1

        elif act == actions[1]:
            n1 = subtract(n1, n2)
            result = n1


        elif act == actions[2]:
            n1 = multiply(n1, n2)
            result = n1


        elif act == actions[3]:
            while n2 == 0:
                print("ERROR: cannot divide by 0")
                n2 = float(input("enter valid number: "))
            n1 = divide(n1, n2)
            result = n1

        elif act == actions[4]:
            result = square_root(n1)


        elif act == actions[5]:
            n1 = power(n1, n2)
            result = n1

        elif act == actions[6]:
            clear(n1, n2)
            n1 = float(input("enter new number: "))
            result = n1

        # elif act == actions[7]:
        #     n2 = redo(n2)


        n1 = result

        if act != actions[7]:
            act = input("another action: ")
            if len(act) != 1:
                print("invalid action")
                act = input("enter a valid action: ")
        while act == actions[6]:
            clear(n1, n2)
            n1 = float(input("enter new number: "))
            result = n1
            act = input("enter new action: ")
        if act != actions[7] and act != actions[4]:
            n2 = float(input("enter another number: "))


while True:
    calculate(num1, action, num2)
