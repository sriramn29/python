a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 11
mul = 1
for i in range(len(a)):
    mul = mul * a[i]
remainder = mul % n
print(remainder)