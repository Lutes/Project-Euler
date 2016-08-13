#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum = 0
squareSum = 0
for x in range(1,101):
	sum += x
	squareSum += x * x
sum = sum * sum
answer =  sum  - squareSum
print "The answer to question 6 is: ", answer