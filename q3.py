#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

key = 600851475143
i = 2

while i * i < key:
 	while key % i == 0:
 		key = key / i
 	i = i + 1

print "The answer to question 3 is: " + str(key)