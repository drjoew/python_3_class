#This is an example of a non working program
#Please debug this program until it works

global x

def x_sqrd():
    global x
    x = x*x
    return x

def x_cubed(w):
    x = ((w)*(w)*(w)-1)
    return

for x in range (0,10)
    y = x_sqrd()
    z = x_cubed(x)
    print("For the number",x,"It's square is: ",y, "and its cube is:", z)

i=10
while i<=120:
    sq_root_i = i**(1/2)
    print ('for the number:","%4.0d"% i,"the square root is", "%5.3f"% sq_root_i)
    i=i+10

