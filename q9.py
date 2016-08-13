#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

answer = 0
for a in range(1, 500):
    for b in range(1, 500):
        for c in range(0, 500):
            if ((a+b+c == 1000) and (a*a + b*b == c*c)):
                answer = a * b * c
                break
        else:
            continue
        break
    else:
        continue
    break
print "The answer to question 9 is: ", answer