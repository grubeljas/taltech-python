"""This program asks user about his name and year of birth.
/n Then it says how old user was when Python 3.0 was released."""

name = input("What is your name?")
year = int(input("Hello, " + name + "! What year were you born in?"))

if int(year) <= 2008:
    print("You were " + str(2008 - year) + ' years old when Python 3.0 was released')
else:
    print("Python 3 was " + str(year - 2008) + " years old when you were born.")
