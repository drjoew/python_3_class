#This is a solution to the non working program
# It is not the only solution
#It now runs

#global x

def x_sqrd(x):
    #global x
    x = x*x
    return x

def x_cubed(w):
    x = ((w)*(w)*(w))
    return x

for i in range (0,10):
    y = x_sqrd(i)
    z = x_cubed(i)
    print("For the number",i,"It's square is: ",y, "and its cube is:", z)

i=10
while i<=120:
    sq_root_i = i**(1.0/2.0)
    print ("for the number:","%4.0d"% i,"the square root is", "%5.3f"% sq_root_i)
    i=i+10

