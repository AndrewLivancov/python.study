import numpy as np 
arr = np.array([1,2,3,4,5,6,7])
filter_arr = []
for element in arr:
	if element % 2 == 0:
		filter_arr.append(True)
	else:
		filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)