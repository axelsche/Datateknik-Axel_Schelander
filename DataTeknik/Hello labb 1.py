def square(x):
    return (x*x)

def circle(x):
    return(x*x*3.14)

x = 0

input_shape = input("what shape is the object? square or circle")
user_input = input("what is the radius/side length: ")

# Converting the input string to an integer
x = int(user_input)

areaS = (x*x)
areaC = (x*x*3.14)

if input_shape == square:
    print (areaS)
else:
    print(areaC)


