"""This program works on Linux, Windows 8.1 and OS X
It is the same as the window 8.1 version
"""

import os                                       # import the library
import platform
s= os.name                                      #fingerprint operating system
print ("Operating System is ", s)
os_name = platform.uname()                            # get more details about OS
for j in range (0, 5):
    print(os_name[j])

directory = os.popen('cd').readlines()         #read current directory
                                                # set up command for each OS
print("\nCurrent directory is: ", directory)
if s == 'posix' :                               #start of if s == 'posix'
    cmd='ifconfig'
elif s == 'nt' :
    cmd = 'ipconfig'
else:
    print ("Unknown Operating System")          #end of if s == 'posix'

if (s == 'posix' or s == 'nt') :                # start of if (s == 'posix' or s == 'nt')   
    state_network = os.popen(cmd).readlines()
    print("network state is:")
    a= len(state_network)
 
    for i in range (0,a):
        print(state_network[i],end='')         # print state of network
else:
    print ("Command not run")                   #end if (s == 'posix' or s == 'nt')

    
