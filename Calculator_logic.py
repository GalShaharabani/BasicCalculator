from Calculator import Calculator

print("Welcome!")
num1 = float(input("enter first number: "))
num2 = 0
action = input("action: ")
valid_action = True
actions = Calculator.load_actions(Calculator.actions)
if action == actions[4]:
    num2 =0

while len(action) != 1 or action not in actions:
    valid_action = False
    print("invalid action")
    action = input("enter a valid action: ")

    if len(action) == 1:
        valid_action=True

if valid_action and action != actions[4]:
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
                result = Calculator.add(number1, number2)


            elif act == actions[1]:
                result = Calculator.subtract(number1, number2)


            elif act == actions[2]:
                result = Calculator.multiply(number1, number2)


            elif act == actions[3]:
                while number2 == 0:
                    print("ERROR: cannot divide by 0")
                    number2 = float(input("enter valid number: "))
                result = Calculator.divide(number1, number2)


            elif act == actions[4]:
                result=Calculator.square_root(number1)



            elif act == actions[5]:
                result=Calculator.power(number1,number2)


            elif act == actions[6]:
                Calculator.clear(number1,number2)
                result = float(input("enter new number: "))

            elif act == actions[7]:
                result = Calculator.repeat(number1,number2,act)


            number1 = result

            if act != actions[8]:
                act = input("another action: ")
                if len(act) != 1 or act not in actions:
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
