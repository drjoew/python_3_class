for i in range (0,256):
    print ("The number ", "%5d"% i, "is", "%5o"% i, "in octal and", "%X"% i, "in upper case hexadecimal and", "{0:8b}".format(i), "in binary")
