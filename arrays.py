cars = ["Ford", "Volvo", "BMW"]
print(cars)
x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars)
x = len(cars)
print(x)
for x in cars:
	print(x)
cars.append("Honda")
print(cars)
cars.pop(1)
print(cars)
cars.remove("Honda")
print(cars)