def main():
    triangle = make_triangle()
    perimeter_of_triangle = triangle_perimeter(triangle)
    print(f'The perimeter of the triangle is {perimeter_of_triangle}')

def make_triangle()->tuple:
    side_1 = float(input('What is the length of side 1? '))
    side_2 = float(input('What is the length of side 2? '))
    side_3 = float(input('What is the length of side 3? '))
    return (side_1, side_2, side_3)

def triangle_perimeter(triangle: tuple)->float:
    perimeter = 0.0
    for side in triangle:
        perimeter += side
    return perimeter

if __name__ == "__main__":
    main()