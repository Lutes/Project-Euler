#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

primes = [2,3,5]
x = 5
key =  0
while (len(primes) < 10001):
	for i in range(0, len(primes)):
		if (x % primes[i] == 0):
			key = 0
			break
		else:
			key = 1
			continue
		
	if (key == 1): 
		primes.append(x)

	x+=1;
print "The answer to question 7 is: ", primes[len(primes)-1]