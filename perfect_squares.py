#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Dec 2019
# This is program exponents printer


def perfectSquare(number):
    # This takes value and makes perfect square

    # process
    square = number * number

    # output
    return square


def on_all(function, a_list):
    # This runs a given function on every item of a given list

    # This is declaring the new number list
    new_list = []

    # process
    for item in a_list:
        new_number = function(item)
        new_list.append(new_number)

    # process
    return new_list


def main():
    # This creates a list, fils it with 1-20 and calls OnAll()

    # This is a list to hold the 20 numbers
    numbers = []

    # This is a list to hold the perfect squares of the first 20 numbers
    perfect_squares = []

    # This welcomes user
    print("This prints the first 20 perfect squares")

    # process
    for repeater in range(1, 21):
        numbers.append(repeater)

    # This'll run PerfectSquares() on every item of numbers, a list, and assign
    #    all of that into perfectSquares, the final numbers
    perfect_squares = on_all(perfectSquare, numbers)
    print("\nThe perfect squares are: ")
    for number in perfect_squares:
        print(number)


if __name__ == "__main__":
    main()
