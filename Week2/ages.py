def main():
    print(ages())

def ages()->str:
    name_anton = 'Anton'
    name_beth = 'Beth'
    name_chen = 'Chen'
    name_drew = 'Drew'
    name_ethan = 'Ethan'

    age_anton = 21
    age_beth = age_anton + 6
    age_chen = age_beth + 20
    age_drew = age_chen + age_anton
    age_ethan = age_chen
    
    names_ages = f'{name_anton} is {age_anton} years old.\n'\
        f'{name_beth} is {age_beth} years old.\n'\
        f'{name_chen} is {age_chen} years old.\n'\
        f'{name_drew} is {age_drew} years old.\n'\
        f'{name_ethan} is {age_ethan} years old.'
    
    return names_ages

if __name__ == '__main__':
    main()