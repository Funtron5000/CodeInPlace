import random

def main():
    #for i in range(20):
    #    print(f'Coin flip {i} is: {flip_coin()}')
    print('Coin is flipped....\n...\n...')
    print(f'The result is {flip_coin()}')

def flip_coin()->str:
    toss = random.randint(1,10)
    if toss < 8:
        return 'heads'
    else:
        return 'tails'

if __name__ == "__main__":
    main()