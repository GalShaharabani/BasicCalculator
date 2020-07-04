from Calculator import Calculator
import sys, time

print("Welcome!")
num1 = float(input("enter first number: "))
num2 = 0
action = input("action: ")
valid_action = True
actions = Calculator.load_actions(Calculator, Calculator.actions)
shtdwn="e"
if action == actions[4] or action == actions[7]:
    num2 =0
if action == shtdwn or action == shtdwn.upper():
    dot = ['.', '..', '...']
    for i in range(3):
        print("Shutting down" + dot[i])
        time.sleep(1)
    print("Goodbye!")
    sys.exit(0)
while len(action) != 1 or action not in actions or len(action) == 0:
    valid_action = False
    print("invalid action")
    action = input("enter a valid action: ")

    if len(action) == 1:
        valid_action=True

if valid_action and action != actions[4] and action != actions[7] :
    num2 = float(input("enter second number: "))


def calculate(number1, act, number2, actions):
        result = 0
        while act != actions[0] and act != actions[1] and act != actions[2] and act != actions[3] \
                and act != actions[4] and act != actions[5] and act != actions[6] and act != actions[7]:
            print(str(act) + " is not an action")
            act = input("enter a valid action: ")
            number2 = float(input("enter another number: "))

        # for act in actions:
        #     i=0
        #     if act not in actions:
        #         print(str(act) + " is not an action")
        #         act = input("enter a valid action: ")
        #         number2 = float(input("enter another number: "))
        #     i+=1
        # number2 = number2
        while True:

            if act == actions[0]:
                try:
                    result = Calculator.add(Calculator, number1, number2)
                except TypeError:
                    print("Error with Add func")

            elif act == actions[1]:
                try:
                    result = Calculator.subtract(Calculator, number1, number2)
                except TypeError:
                    print("Error with Subtruct func")


            elif act == actions[2]:
                try:
                    result = Calculator.multiply(Calculator, number1, number2)
                except TypeError:
                    print("Error with Multiply func")


            elif act == actions[3]:
                while number2 == 0:
                    print("ERROR: cannot divide by 0")
                    number2 = float(input("enter valid number: "))
                try:
                    result = Calculator.divide(Calculator, number1, number2)
                except TypeError:
                    print("something went wrong")


            elif act == actions[4]:
                try:
                    result = Calculator.square_root(Calculator, number1)
                except TypeError:
                    print("something went wrong")



            elif act == actions[5]:
                try:
                    result = Calculator.power(Calculator, number1, number2)
                except TypeError:
                    print("something went wrong")


            elif act == actions[6]:
                Calculator.clear(Calculator, number1,number2)
                result = float(input("enter new number: "))

            # elif act == actions[7]:
            #     try:
            #         result = Calculator.repeat(number1, number2, act)
            #     except TypeError:
            #         print("something went wrong")


            number1 = result

            if act != actions[7]:
                act = input("another action: ")
                if act == shtdwn or action == shtdwn.upper():
                    dot = ['.', '..', '...']
                    for i in range(3):
                        print("Shutting down"+dot[i])
                        time.sleep(1)
                    print("Goodbye!")
                    sys.exit(0)
                elif len(act) != 1 or act not in actions or len(act) == 0:
                    print("invalid action")
                    act = input("enter a valid action: ")

            while act == actions[6]:
                Calculator.clear(number1,number2)
                result = float(input("enter new number: "))
                number1 = result
                act = input("enter new action: ")
            if act != actions[7] and act != actions[4]:
                number2 = float(input("enter another number: "))

while True:
    calculate(num1,action,num2,actions)
