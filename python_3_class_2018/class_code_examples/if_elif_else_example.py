# example for if elif else
temperature = 0.0
scale = "C"
if (scale == "F"):
    print("Temperature is ", "%10.2f"% temperature, "degrees Farenheit")
    print("Temperature is ", "%10.2f"% ((temperature-32.0)*(5.0/9.0)), "Degrees Centigrade")
    print("Temperature is ", "%10.2f"% ((temperature-32.0)*(5.0/9.0)+273.15), "Kelvin")
elif(scale == "C"):
    print("Temperature is ", "%10.2f"% ((temperature*9.0/5.0)+32.0), "degrees Farenheit")
    print("Temperature is ", "%10.2f"% temperature, "Degrees Centigrade")
    print("Temperature is ", "%10.2f"% (temperature+273.15), "Kelvin")
elif (scale == "K"):
    print("Temperature is ", "%10.2f"% ((temperature-273.15)*(9.0/5.0)+32.0), "degrees Farenheit")
    print("Temperature is ", "%10.2f"% (temperature-273.15), "Degrees Centigrade")
    print("Temperature is ", "%10.2f"% temperature, "Kelvin")
else:
    print("Wrong scale specified")
print("Conversion Complete")
