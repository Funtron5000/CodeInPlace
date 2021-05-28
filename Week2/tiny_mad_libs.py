
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    adjective = get_adjective()
    noun = get_noun()
    verb = get_verb()
    print(f'{SENTENCE_START} {adjective} {noun} {verb}')

def get_adjective()->str:
    return input('Please type an adjective and press enter. ')

def get_noun()->str:
    return input('Please type a noun and press enter. ')

def get_verb()->str:
    return input('Please type a verb and press enter. ')

if __name__ == "__main__":
    main()
