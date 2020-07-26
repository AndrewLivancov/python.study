import json

x = {
	"name": "John",
	"age": 30,
	"married": True,
	"divorced": False,
	"children": ("Ann", "Billy"),
	"pets": None,
	"cars": [
		{"model": "BMW 230", "mpg": 27.5},
	   ]
	}

print(json.dumps(x, indent=4))