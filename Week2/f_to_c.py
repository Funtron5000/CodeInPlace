def main():
    fahrenheit = float(input('Enter temperature in Fahrenheit: '))
    celsius = degrees_celsius(fahrenheit)
    print(f'Temperature: {fahrenheit}F = {celsius}C')

def degrees_celsius(fahrenheit: float)->float:
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    main()