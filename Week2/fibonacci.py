
MAX_VALUE = 10000

def main():
    num_0 = 0
    num_1 = 1
    print(f'{num_0}')
    fib(num_0, num_1)

def fib(num_0: int, num_1: int)->None:
    print(f'{num_1}')
    new_num = num_0 + num_1
    if new_num < MAX_VALUE:
        fib(num_1, new_num)
        

if __name__ == "__main__":
    main()