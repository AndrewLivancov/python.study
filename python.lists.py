thislist = ["apple", "banana", "cherry"]
print(thislist)
#Access second Item of the element:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Negative indexing means beginning from
# the end, -1 refers to the last item
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#returns the items from the beginning to "orange":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#returns the items from "cherry" and to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#Range of Negative Indexes:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)
#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
	print(x)
#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
	print("Yes 'apple' is in the fruits list")
#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#Add Items Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#The pop() method removes the specified index,
#(or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#The del keyword can also delete the list completely:
#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#Append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
	list1.append(x)

print(list1)
#extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#The list() Constructor
#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry"))
print(thislist)