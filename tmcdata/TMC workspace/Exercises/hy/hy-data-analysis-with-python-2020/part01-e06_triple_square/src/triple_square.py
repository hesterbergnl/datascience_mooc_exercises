#!/usr/bin/env python3

def triple(x):
    "Multiplies the value x by 3"
    return x*3

def square(x):
    "Squares the value of x"
    return x*x

def main():
    for i in range(1, 11):
        squareVal = square(i)
        tripleVal = triple(i)

        if(squareVal <= tripleVal):
            print("triple({:d})=={:d} square({:d})=={:d}".format(i,tripleVal,i,squareVal))
        else:
            break

if __name__ == "__main__":
    main()
