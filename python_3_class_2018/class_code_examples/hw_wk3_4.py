"""This program reads a csv file and then prints out the data
we first learn that using csv messed up the data since
number greater than 999 had commas added to them
Also three lines have missing commas
If this was a one time project, we could fix the data
in another program like a text editor and get rid of the extra commas
But most likely if this was a real project we have to account
for bad data
So we will try to read the data and fix it up
Looking at the data in a spread sheet program we find that
There are five colums of data
year month dow nasdq S&P
So we need to get the data in this format even though
because of the extra commas there are 8 columns
"""
import os
import re  # regular expression library see comments below for why we chose this
directory = os.popen('pwd').readlines()         #read current directory
                                                # set up command for each OS
print("\nCurrent directory is: ", directory[0])

f = open('stock_data.csv', 'r')
stock_data=[]
comma_add=","
i=0
for line in f:
    stock_data.append( line)
    #print (line)
    i=i+1
#for i in range(0,len(stock_data)):
#    print(stock_data[i])
# Now we have the data in a list
# we need to fix up the data
# first we notice that all years are in 4 digit format
# Then we notice that all months are 3 characters long except April
# So we need to change April to Apr to make it 3 characters long
# knowing that there are text editing function in many languages
# we google for string manipulation in python
# and discover there is a regular expression library re
# which is a text editing function
# https://docs.python.org/3/library/re.html#text-munging
# we can now use the re.sub() to remove the "il" from each line that has
# April thus converting it to Apr
for i in range(0,len(stock_data)):
    stock_data[i] = re.sub("il","",stock_data[i])
    #print(stock_data[i])
# Success now we have consistent data lengths for the first two elements of each line
#
"""Next let us fix the missing commas
we notice for the range of the data we have,
the dow values are           9 characters in length including the "," and "."
the nasdq and S&P values are 8 characters in length including the "," and "."
We realize this will not always be true but for the data range we have
it is true
we make a possibly bad decision!
We will make it work with the data we have and add additional
features at the next release
If the market suddently crashes or jumps up
We will get a lot of overtime (hopefully paid) :-) to fix the issue
Life is rough be we need to get the code written by Thursday and today
is Tuesday
"""
#
#
"""First let us fix the missing commas in the xx,xxx.yy field
when there is a missing comma, the field looks like xxxxx.yy we want it to be xx,xxx.yy
We notice that
the bad field is ,xxxxx.yy but should be ,xx,xxx.yy
so we search for ,
As we look in the https://docs.python.org/3/library/re.html
we find that
[] is     Used to indicate a set of characters. In a set:
so [0-9] matches all number is one digit
so we want to find ,[0-9][0-9][0-9] and insert a comma in between the second and third digit
We know that the start of the first digit is in the 10th location starting the count at 0
if it is a digit, we want to insert a comma
"""
print("Find missing , in dow data\n\n")
for i in range(0,len(stock_data)):
    if re.search("[,][0-9][0-9][0-9][0-9][0-9]", stock_data[i]):
        print (stock_data[i])
#stock_data[i] = re.sub("il","",stock_data[i])
#print(stock_data[i])
print ("found them!")

#now we we do this for the missing data in nasdq
print("Find missing , in nasdq data\n\n")
for i in range(0,len(stock_data)):
    if re.search("[,][4-6][0-9][0-9][0-9]", stock_data[i]):
        print (stock_data[i])
#stock_data[i] = re.sub("il","",stock_data[i])
#print(stock_data[i])
print ("found them!")
#
#now we we do this for the missing data in s&p
print("Find missing , in s&p data\n\n")
for i in range(0,len(stock_data)):
    if re.search("[,][1-2][0-9][0-9][0-9]", stock_data[i]):
        print (stock_data[i])
#stock_data[i] = re.sub("il","",stock_data[i])
#print(stock_data[i])
print ("found them!")
#
# noticed we cheated again by using the range of the first digit for each data set
# if the values go outside the range, we will need to fix the code


# now that we know we can find them, let's fix them
# we would do this in one step but I am doing it separately to show how it is done

print("Fix missing , in dow data\n\n")
for i in range(0,len(stock_data)):
    if re.search("[,][0-9][0-9][0-9][0-9][0-9]", stock_data[i]):
        temp_data =str(stock_data[i])
        stock_data[i] = temp_data[0:11] +comma_add + temp_data[12:len(temp_data)]        
        print (stock_data[i])
#stock_data[i] = re.sub("il","",stock_data[i])
#print(stock_data[i])
print ("Fixed them!")

#now we we do this for the missing data in nasdq
print("Fix missing , in nasdq data\n\n")
for i in range(0,len(stock_data)):
    if re.search("[,][4-6][0-9][0-9][0-9]", stock_data[i]):
        temp_data =str(stock_data[i])
        stock_data[i] =  str(temp_data[0:20]) +str(comma_add) + str(temp_data[20:len(temp_data)]) 
        print (stock_data[i])
#stock_data[i] = re.sub("il","",stock_data[i])
#print(stock_data[i])
print ("Fixed them!")
#
#now we we do this for the missing data in s&p
print("Fix missing , in s&p data\n\n")
for i in range(0,len(stock_data)):
    if re.search("[,][1-2][0-9][0-9][0-9]", stock_data[i]):
        temp_data=stock_data[i]
        stock_data[i] = str(temp_data[0:29]) +str(comma_add) + str(temp_data[29:len(temp_data)]) 
        print (stock_data[i])
#stock_data[i] = re.sub("il","",stock_data[i])
#print(stock_data[i])
print ("Fixed them!")

#Now let's print it out formatted
print("Year   Month     Dow         NASDQ       S&P")

for i in range(1,len(stock_data)):
    temp_data = str(stock_data[i])
    print(temp_data[0:4],"  ", temp_data[5:8],"  ",temp_data[9:18],"  ", temp_data[19:27], "  ", temp_data[28:len(temp_data)], end="") 

# adding end ="" eliminated the new line at the end since the string already had a new line


