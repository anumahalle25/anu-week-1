# Write a program to create a function that takes two numbers and an operator as arguments and returns the result of the operation (+, -, *, /)

def calculate(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    else:
        return n1 / n2


    print((calculate ( 10, 30, "+")))
    print((calculate (10, 30, "-")))
    print((calculate (10, 30, "*")))
    print((calculate (10, 30, "/")))    