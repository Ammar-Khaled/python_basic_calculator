print("Welcome to our Basic Calculator!")
print("we support addition, subtraction, multiplication, division, remainder and Exponentiation")

# List of supported operators
operators = ['+', '-', '*', '/', '%', '^']

while True:
    #prompt user to get input
    ex = input("Enter your mathematical expression in form of 'num1 operator num2': ")
    ex = ex.split(" ")
    num1 = int(ex[0])
    op = ex[1]
    num2 = int(ex[2])
    if op == operators[0]:
        print("result = {0}".format(num1 + num2))
    elif op == operators[1]:
        print("result = {0}".format(num1 - num2))
    elif op == operators[2]:
        print("result = {0}".format(num1 * num2))
    elif op == operators[3]:
        print("result = {0}".format(float(num1) / num2))
    elif op == operators[4]:
        print("result = {0}".format(num1 % num2))
    elif op == operators[5]:
        print("result = {0}".format(num1 ** num2))
    else:
        print("Unsupported operation :(")
    flag = input("Do you want to try again (yes/no)? ")
    if flag.lower() == "no":
        break
