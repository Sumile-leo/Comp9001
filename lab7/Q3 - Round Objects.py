# Write a program geometry.py that computes the area of a circle and the volume
# of a sphere with a radius taken from input.
#
# First, implement the functions get_area  and get_volume.
#
# get_area: Takes in one parameter radius and calculates the area of a circle using the  formula:
# A=PI*R*R

# get_volume: Takes in one parameter radius and calculates the volume of a sphere using the formula:
# V=4*PI*R*R*R/3

# Then, fix the code inside the main function to correctly get the radius, calculate
# the area and volume and output it to 3 decimal places.
#
# Enter radius: 2.5
# Area: 19.635
# Volume: 65.450

import math

# use this value to help with your calculations!
PI = math.pi

def get_area(radius: float) -> float:
    '''
    Calculates the area of a circle.

    Parameters:
    radius (float): radius of circle

    Returns:
    float: area of circle
    '''
    return PI * radius ** 2
    pass

def get_volume(radius: float) -> float:
    '''
    Calculates the volume of a sphere.

    Parameters:
    radius (float): radius of sphere

    Returns:
    float: volume of sphere
    '''
    return (PI * radius ** 3)*4/3
    pass

def main():
    radius = float(input('Enter radius: '))
    area = get_area(radius)
    volume = get_volume(radius)
    print(f'Area: {area:.3f}')
    print(f'Volume: {volume:.3f}')

if __name__ == '__main__':
	main()