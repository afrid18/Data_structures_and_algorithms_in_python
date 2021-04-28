# Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output
# device. That is, each input to the calculator, be it a number, like 12.34
# or 1034, or an operator, like + or =, can be done on a separate line. After
# each such input, you should output to the Python console what would be displayed on your calculator.

## Code for the above question



while True:
    input1 = input()
    print(input1)
    operator = ['+', '-', '*', '/']
    lis = []
    lis = input1.split(' ')
    for element in lis:
        temp = element
"""
while True:
  input1=input('Enter Expression:')
  list1=[]
  a=[]
  list1 = input1.split()
  a.insert(0,int(list1[0]))
  a.insert(1,int(list1[2]))
  if '+' in list1:
    temp= a[0]+a[1]
  elif '-' in list1:
    temp= a[0]-a[1]
  elif '*' in list1:
    temp= a[0]*a[1]
  elif '/' in list1:
    temp= a[0]/a[1]
  print(temp)

"""
