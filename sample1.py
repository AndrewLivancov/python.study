thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[2:5])
print(thistuple1[-4:-1])
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
thistuple2 = ("apple", "banana", "cherry")
for x in thistuple2:
	print(x)
if "apple" in thistuple:
	print("Yes, 'apple' is in the fruits tuple")
	print(len(thistuple))
thistuple3 = ("apple",)
print(type(thistuple3))	
# NOT a tuple
thistuple3 = ("apple")
print(type(thistuple3))
tuple4 = (1, 2, 3)
tuple5 = thistuple + tuple4
print(tuple5)
thistuple6 = tuple(("apple", "banana", "Cherry"))
print(thistuple6)