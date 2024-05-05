import time                     # import entire time library
from time import localtime      # import only localtime from time library
from time import sleep          # import only sleep from time library
t = time.localtime()            # local time is a structure[year, month,
                                # day, hour, min, sec, day of week, day of year, dst on off]
print(t[3],":",t[4],":",t[5])   # hour minutes, seconds
time.sleep(2)                   # sleep for 2 seconds
t1=localtime()
print("%d"%t1[3],":",t1[4],":",t1[5])
sleep(5)
t1=localtime()
print("%d"%t1[3],":",t1[4],":",t1[5])
