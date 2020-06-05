#!/usr/bin/env python3

import math

def triangleArea(base, height):
    return (0.5 * base * height)

def rectangeArea(width, length):
    return (length * width)

def circleArea(radius):
    return (math.pi * radius * radius)

def main():
    while(True):
        userInput = input("Choose a shape (triangle, rectangle, circle): ")
        if(userInput == "triangle"):
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            print("The area is {:.6f}".format(triangleArea(base, height)))
        elif(userInput == "rectangle"):
            width = float(input("Give width of the rectangle: "))
            length = float(input("Give height of the rectangle: "))
            print("The area is {:.6f}".format(rectangeArea(width, length)))
        elif(userInput == "circle"):
            radius = float(input("Give radius of the circle: "))
            print("The area is {:.6f}".format(circleArea(radius)))
        elif(userInput == ""):
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
