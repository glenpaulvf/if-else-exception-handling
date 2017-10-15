# Glen Paul Florendo
# COMPTNG16
# October 11, 2017

import numbers

# Task 1
def my_divide1(a, b):
	return [x/y for x, y in zip(a, b)]

# Task 2
def my_divide2(a, b):
	if all(isinstance(x, numbers.Number) and isinstance(y, numbers.Number) and y != 0 for x, y in zip(a,b)):
		return [x/y for x,y in zip(a,b)]
	else:
		print "Something's wrong with the inputs to my_divide2"
		return []

# Task 3
def my_divide3(a, b):
	try:
		return [x/y for x,y in zip(a,b)]
	except:
		print "Something's wrong with the inputs to my_divide3"
		return []

# Task 4
def my_divide4(a, b):
	try:
		return [x/y for x,y in zip(a,b)]
	except ZeroDivisionError:
		print "There is a zero in b"
		return []
	except TypeError:
		print "Non-numeric data detected"
		return []

