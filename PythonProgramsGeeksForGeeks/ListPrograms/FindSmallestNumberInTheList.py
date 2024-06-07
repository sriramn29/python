a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# smallest = a[0]
# for i in range(1, len(a)):
#     if a[i] <= smallest:
#         smallest = a[i]
#     else:
#         continue
# print(smallest)

# print(min(a))

# a.sort()
# print(a[0])

print(min(a, key = lambda value: int(value)))