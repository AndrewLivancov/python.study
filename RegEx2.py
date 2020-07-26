import re

txt = "The rain in Spain"

x = re.findall("Portugal", txt)
print(x)

if (x):
	print("YES, there is at least one match!")
else:
	print("NO match")