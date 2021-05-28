
EARTH_MARS_RATIO = 0.378

def main():
    earth_weight = float(input('Enter a weight on Earth: '))
    mars_weight = earth_weight_to_mars(earth_weight)
    print(f'Your entered weight of {earth_weight} lbs. is {mars_weight} lbs. on Mars.')

def earth_weight_to_mars(earth_weight: float)->float:
    return earth_weight * EARTH_MARS_RATIO

if __name__ == '__main__':
    main()