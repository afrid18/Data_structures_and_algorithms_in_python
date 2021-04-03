##  Project 1.29
# Write a Python program that outputs all possible strings formed by using thecharacters c , a , t , d , o ,and g exactlyonce.
##

from math import factorial

letters = ['c', 'a', 't', 'd', 'o', 'g']            # Letters given

size_of_letters = len(letters)

print("There will be ",factorial(size_of_letters),"possibilities to form strings using the given letters")

def print_strings(letters):

