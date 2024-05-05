# example for a function
def f_to_c(f):
    c = (f-32.0)*(5.0/9.0)
    return c

def c_to_f (c):
    f = c*9.0/5.0+32.0
    return f

def c_to_k(c):
    k = c + 273.15
    return k

def k_to_c(k):
    c = k - 273.15
    return c

def f_to_k(f):
    k = (f-32.0)*(5.0/9.0) + 273.15
    return k

def k_to_f(k):
    f = (k-273.15)*(9.0/5.0)+32.0
    return f
         
         
temperature = 0.0
scale = "K"
if (scale == "F"):
    print("Temperature is ", "%10.2f"% temperature, "degrees Farenheit")
    print("Temperature is ", "%10.2f"% f_to_c(temperature), "Degrees Centigrade")
    print("Temperature is ", "%10.2f"% f_to_k(temperature), "Kelvin")
elif(scale == "C"):
    print("Temperature is ", "%10.2f"% c_to_f(temperature), "degrees Farenheit")
    print("Temperature is ", "%10.2f"% temperature, "Degrees Centigrade")
    print("Temperature is ", "%10.2f"% c_to_k(temperature), "Kelvin")
elif (scale == "K"):
    print("Temperature is ", "%10.2f"% k_to_f(temperature), "degrees Farenheit")
    print("Temperature is ", "%10.2f"% k_to_c(temperature), "Degrees Centigrade")
    print("Temperature is ", "%10.2f"% temperature, "Kelvin")
else:
    print("Wrong scale specified")
print("Conversion Complete")


