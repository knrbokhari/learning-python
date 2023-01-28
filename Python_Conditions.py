# If statements
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Else
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Elif
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("b is not greater than a")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

# multiple else statements on the same line:
print("A") if a > b else print("=") if a == b else print("B")

# Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

if b > a:
  pass