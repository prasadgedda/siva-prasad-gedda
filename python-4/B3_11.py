#B3_11

data = (10, 20, [30, 40], 50)
print("Before modification:", data)
data[2].append(50)
print("After modification:", data)

#OUTPUT:
#Before modification: (10, 20, [30, 40], 50)
#After modification: (10, 20, [30, 40, 50], 50)

