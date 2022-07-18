#!/usr/bin/python3

"""dividing an integer"""
def safe_print_division(a, b):
    que = 0
    try:
        quo = a / b
    except(ZeroDivisionError):
        quo = None
    finally:
        print("Inside result: {}".format(quo))
        return 
