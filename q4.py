#Find the largest palindrome made from the product of two 3-digit numbers.

answer = 0

def isPalindrome(x):
	x = str(x)
	for i in range(0,len(x)):
		if (x[i] != x[len(x) - (i+1)]):
			return False
	
	return True

for i in range(1,1000):
	for j in range(1,1000):
		x = i * j
		if ((isPalindrome(x)) and (x > answer)):
			answer = x

print "The answer to question 4 is: " + str(answer)