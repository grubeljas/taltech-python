"""This program shows how old you had been when Python 3 was released."""

name = input("What is your name?")
year = int(input("Hello, " + name + "! What year were you born in?"))
python_age = str(year - 2008)
persons_age = str(2008 - year)

if int(year) <= 2008:
    print("You were " + persons_age + ' years old when Python 3.0 was released')
else:
    print("Python 3 was " + python_age + " years old when you were born.")
