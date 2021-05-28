
SPEED_OF_LIGHT = 299792458

def main():
    mass = float(input('Enter kilos of mass: '))
    calc_emc(mass)

def calc_emc(mass: float)->None:
    print('e = m * C^2...')
    print(f'm = {mass} kg')
    print(f'C = {SPEED_OF_LIGHT}')
    energy = mass * SPEED_OF_LIGHT**2
    print(f'{energy} joules of energy!')

if __name__ == "__main__":
    main()