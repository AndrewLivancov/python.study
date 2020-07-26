b = "Hello World!"
print(b[2:5])
# Negative Indexing
b = "Hello World!"
print(b[-5:-2])
#String Length
a = "Hello, World!"
print(len(a))
#String Methods
#The strip() method removes any 
#whitespace from the beginning
# or the end:
a = "   Hello,   World!     "
print(a.strip())
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#The replace() method replaces a string 
#with another string:
a = "Hello World!"
print(a.replace("H", "J"))
#The split() method splits the string into substrings
# if it finds instances of the separator:
a = "Hello, World!"
b = a.split(",")
print(b)
#Check String
#Check if the phrase "ain" is present in the 
#following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
#Check if the phrase "ain" is 
#NOT present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)
#String Concatenation
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#String Format
#we cannot combine strings and numbers like this:
#age = 36
#txt = "My name is John, I am " + age
#format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#format() method takes unlimited number of arguments
quantity = 3
itemno = 567
price = 49.65
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#can use index numbers {0}
quantity = 3
itemno = 567
price = 49.65
myorder = "I want to pay {2} dollars for {0} pieces of items {1}."
print(myorder.format(quantity, itemno, price))
#Escape Character
#The escape character allows you to use double 
#quotes when you normally would not be allowed:
txt = "We are the so-called \"Vilings\" from the north."
print(txt)