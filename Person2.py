class Person:
	def __init__(mySillyobject, name, age):
		mySillyobject.name = name
		mySillyobject.age = age

	def myfunc(abc):
		print("Hello my name is " + abc.name)
p = Person("John", 36)
p.myfunc()
p.age = 40
print(p.age)