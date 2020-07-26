a = 200
b = 33

if b > a:
	print("b is greater than a")
elif  a == b:
	print("a and b are equal")
else:
	print("a is greater than b")
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
a1 = 330
b1 = 330
print("A") if a1 > b1 else print("=") if a1 == b1 else print("B")
c = 500
if  a > b and c > a:
	print("Both conditions are True")
if a > b or a > c:
	print("At least one of the conditions is True")
x = 41

if x > 10:
	print("Above ten,")
	if x > 20:
		print("and also above 20!")
	else:
		print("but not above 20.")