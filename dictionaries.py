thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
thisdict['year'] = 2018
print(thisdict)
for x in thisdict:
	print(x)
for x in thisdict:
	print(thisdict[x])
for x in thisdict.values():
	print(x)
for x, y in thisdict.items():
	print(x, y)
if "model" in thisdict:
	print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(thisdict))
thisdict["color"] = "red"
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["brand"]
print(thisdict)
thisdict.clear()
print(thisdict)