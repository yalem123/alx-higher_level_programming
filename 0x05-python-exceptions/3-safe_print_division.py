#!/usr/bin/python3
def safe_print_division(a, b):
    num1, num2 = input("enter values : ").split()
    try:
        quo = int(num1) / int(num2)
        print("{} / {} = {}" .format(num1, num2, quo))
    except(ZeroDivisionError):
        print("u cant divide by zero")
    finally:
        print("i hope its sucess")
        return quo
