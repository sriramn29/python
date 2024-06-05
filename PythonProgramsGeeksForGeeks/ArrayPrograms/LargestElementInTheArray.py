a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(a))
largest = 0
for i in range(len(a)):
    if(a[i] >= largest):
        largest = a[i]
    else:
        continue
print(largest)