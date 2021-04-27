# Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output device. That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be done on a separate line. After each such input, you should output to the Python console what would be displayed on your calculator.

## Code for the above question



while True:
    input1 = input()
    operator = ['+', '-', '*', '/']
    lis = []
    lis = input1.split(' ')
    for element in lis:
        temp = element

