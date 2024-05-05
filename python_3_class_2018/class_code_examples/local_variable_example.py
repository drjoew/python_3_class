# example for local variables
def x_sqrd(x):
    x = x*x
    print("x inside the function is", x)
    return x


x=25.0
print("x outside the function is", x)
y = x_sqrd(x)
print("y outside the function is", y)
print("x outside the function is", x)
