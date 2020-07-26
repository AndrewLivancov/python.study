print(10 > 9)
print(10 == 9)
print(10 < 9)
#message based on the condition is True or False:
a = 200
b = 33

if b > a:
	print("b is greater than a")
else:
	print("b is not greater than a")
#Evaluate Values and Variables
#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))
#Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#Most Values are True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
#Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
#class with a __len__ function that returns 0 or False:
class myclass():
	def __len__(self):
  		return 0
myobj = myclass()
print(bool(myobj))
#Functions can Return a Boolean
def myFunction() :
	return True

print(myFunction())
#Print "YES!" if the function 
#returns True, otherwise print "NO!":
def myFunction() :
	return True

if myFunction():
	print("YES!")
else:
	print("NO!")
#Check if an object is an integer or not:
x = 200
print(isinstance(x, int))