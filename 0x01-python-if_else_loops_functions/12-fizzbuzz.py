#!/usr/bin/python3
def fizzbuzz():
    """Prints the numbers from 1 to 100 seperated by space
       For multiples of three print 'Fizz' instead of the number and for
       multiples of five print 'Buzz'.
       For numbers which are multiples of both three and five print 'FizzBuzz'
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz ", end='')
        elif num % 3 == 0:
            print("Fizz ", end='')
        elif num % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(num), end='')
