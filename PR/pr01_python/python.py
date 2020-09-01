"""This program asks user about his name and year of birth.
/n Then it says how old user was when Python 3.0 was released"""

name = input("What is your name?")
year = int(input("Hello, " + name + "! What year were you born in?"))
persons_age = str(2008 - year)
python_age = str(year - 2008)

if int(year) <= 2008:
    print("You were " + persons_age + ' years old when Python 3.0 was released')
else:
    print("Python 3 was " + python_age + " years old when you were born.")
