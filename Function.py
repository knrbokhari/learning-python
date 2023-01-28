# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.

# In Python a function is defined using the def keyword:


# Creating a Function
def my_function():
  print("Hello from a function")

# Calling a Function
my_function()

#  Arguments Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil")

# Arbitrary Arguments, *args
def my_function2(*kids):
  print("The youngest child is " + kids[2])

my_function2("Emil", "Tobias", "Linus")

# Default Parameter Value
def my_function3(country = "Norway"):
  print("I am from " + country)

my_function3("BD")
my_function3()









