#Jake White
#Student ID: 101219029

import timeit
from random import randint

#generates n 



n = int(raw_input("n: "))
print "***************BEGIN**************"
start = timeit.default_timer()

def sort(t):
	x = 0 
	k = n-1
	while x < k:
		test = x
		while (test < n):
			
			if(t[x] > t[test]):
				y = t[x]
				t[x] = t[test]
				t[test] = y
			
			test = test + 1
		x = x + 1	

########first iteration######################
print "**************ONE**********************"
array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1

print "******************TWO******************"
##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1
print "******************TWO******************"
print "**********THREE************************"
###############################################

##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1

print "*************FOUR**********************"
##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1

print "*************FIVE**********************"
##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1

print "***************SIX*********************"
##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1

print "************SEVEN**********************"
##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1

print "***************EIGHT*******************"
##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1

print "***************NINE*********************"

##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1

print "*****************TEN*******************"
##############################################

array = [None]*n

i = 0

while (i < n):
	j = randint(1, 1000000)
	array[i] = j
	i = i + 1
	

sort(array)

count = 0

while count < n:
	print array[count]
	count = count + 1



print "******************END******************"



stop = timeit.default_timer()
runT = stop - start
print "Run Time: ", runT











		
