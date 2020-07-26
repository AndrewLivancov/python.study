fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		continue
	print(x)
for x in range(6):
	print(x)

for x in range(2, 6):
	print(x)
for x in range(2, 30, 3):
	print(x)
else:
	print("Finnaly finished!")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
	for y in fruits:
		print(x, y)
for x in [0, 1, 2]:
	pass