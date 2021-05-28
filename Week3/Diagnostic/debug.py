"""
Part A:
This program will print 42, because divide_and_roun()
has no return and n is not being reassigned by the function
divide_and_round must do a return on n
and in main() n = divide_and_round(n) must be used to reassign n
"""

"""
Part B: 
Edit this code so that it works correctly
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        #wrapped assignment in int() function so the number is an integer
        n = int(n / 2)
    else:
        #wrapped assignment in int() function so the number is an integer
        n = int((n + 1) / 2)
    #Adding a return for n so that the number calculated in here can be used elsewhere
    return n

def main():
    n = 42
    #reassigning the value for n using n = divide_and_round
    n = divide_and_round(n)
    print(n)

#Adding if name is main to call main
if __name__ == '__main__':
    main()