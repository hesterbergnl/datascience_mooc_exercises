#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    sqrtPart = math.sqrt((math.pow(b,2) - 4*a*c))
    xA = (-1*b + sqrtPart) / (2 * a)
    xB = (-1 * b - sqrtPart) / (2 * a)
    return (xA,xB)


def main():
    print(solve_quadratic(1,-3,2))

if __name__ == "__main__":
    main()
