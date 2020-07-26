class MyClass:
	x = 5
print(MyClass)
p1 = MyClass()
print(p1.x)
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)
