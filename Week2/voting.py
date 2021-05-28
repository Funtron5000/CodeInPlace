
PETURKSBOUIPO = 16
STANLAU = 25
MAYENGUA = 48

def main():
    age = int(input('How old are you? '))
    global_vote(age)

def vote_peturksbouipo(age: int)->None:
    if age >= PETURKSBOUIPO:
        vote = 'can'
    else:
        vote = 'cannot'
    message = f'vote in Peturksbouipo where the voting age is {PETURKSBOUIPO}.'
    print(f'You {vote} {message}')

def vote_stanlau(age: int)->None:
    if age >= STANLAU:
        vote = 'can'
    else:
        vote = 'cannot'
    message = f'vote in Stanlau where the voting age is {STANLAU}.'
    print(f'You {vote} {message}')

def vote_mayengua(age: int)->None:
    if age >= MAYENGUA:
        vote = 'can'
    else:
        vote = 'cannot'
    message = f'vote in Mayengua where the voting age is {MAYENGUA}.'
    print(f'You {vote} {message}')

def global_vote(age: int)->None:
    vote_peturksbouipo(age)
    vote_stanlau(age)
    vote_mayengua(age)

if __name__ == "__main__":
    main()