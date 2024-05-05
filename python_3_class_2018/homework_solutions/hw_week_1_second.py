# homework second problem solution
""" There are multiple ways to check for temperatures below absolute zero
This is just one of many solutions
Notice that I had to add indents to all the previous statement
to get the code to run correctly
That is because python requires indents to determine proper code flow
"""
temperature = -459.66
scale = "F"


if (scale == "F"):
    temperature_K = ((temperature-32.0)*(5.0/9.0)+273.15)
    if (temperature_K>=0.0):
        print("Temperature is ", "%10.4f"% temperature, "degrees Farenheit")
        print("Temperature is ", "%10.4f"% ((temperature-32.0)*(5.0/9.0)), "Degrees Centigrade")
        print("Temperature is ", "%10.4f"% temperature_K, "Kelvin")
    else:
        print("Temperature below absolute zero; can not calculate temperature")
        
elif(scale == "C"):
    temperature_K=(temperature+273.15)
    if (temperature_K>=0.0):
        print("Temperature is ", "%10.4f"% ((temperature*9.0/5.0)+32.0), "degrees Farenheit")
        print("Temperature is ", "%10.4f"% temperature, "Degrees Centigrade")
        print("Temperature is ", "%10.4f"% temperature_K, "Kelvin")
    else:
        print("Temperature below absolute zero; can not calculate temperature")
        
elif (scale == "K"):
    temperature_K = temperature
    if (temperature_K>=0.0):
        print("Temperature is ", "%10.4f"% ((temperature-273.15)*(9.0/5.0)+32.0), "degrees Farenheit")
        print("Temperature is ", "%10.4f"% (temperature-273.15), "Degrees Centigrade")
        print("Temperature is ", "%10.4f"% temperature_K, "Kelvin")
    else:
        print("Temperature below absolute zero; can not calculate temperature")
else:
    print("Wrong scale specified")
print("Conversion Complete")
