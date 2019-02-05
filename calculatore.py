import re

previous= 0
run= True

def my_function():
    global run
    global previous
    if previous==0:
        equation=input("Enter the equation:")
    else:
        equation=input(str(previous))
    if equation=='quit':
        print('good bye')
    else:
        print("proceeding")
    if previous==0:
      previous=eval(equation)
    else:
       previous=eval(str(previous)+equation)
while run:
    my_function()
