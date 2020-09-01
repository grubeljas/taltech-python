name = input("What is yor name?")
year = int(input("Hello " + name + "! What year were you born in?"))
persons_age = 2008 - year
python_age = year - 2008

if int(year) <= 2008:
    print("You were age " + str(persons_age) + " years old when Python 3.0 was released.")
else:
    print("Python 3 was " + str(python_age) + " years old when you were born.")
