import math

x = input("X:")
y = input("Y:")
z = input("Z:")

print("[", int(z)-int(x) , ", ", -int(y) - math.ceil((int(z) - int(x))/2), "]")

input("Press enter to quit...") 
