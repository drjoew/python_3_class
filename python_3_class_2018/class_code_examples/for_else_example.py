# find all prime numbers between 1 and 100
# if the number is not prime, list its factors
for number in range(1, 101):
    for factor in range(2, number):
        if number % factor == 0:
            print("This number is not prime", "%4d"% number, '=', factor, '*', "%2d"% (number/factor) )
            break
    else:
        # loop fell through without finding a factor
        print('This is a prime number  ', "%4d"% number)
