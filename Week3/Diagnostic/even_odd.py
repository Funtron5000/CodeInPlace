# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    even_odd()

def even_odd():
    for i in range(1, MAX_NUMBER + 1):
        if i % 2 == 0:
            print(f'{i} is even')
        else:
            print(f'{i} is odd')

if __name__ == "__main__":
    main()