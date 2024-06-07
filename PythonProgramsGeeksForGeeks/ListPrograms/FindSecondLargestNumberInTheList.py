a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ac = list(set(a))
# ac.sort()
# ac.reverse()
# print(ac[1])

ac = set(a)
ac.remove(max(ac))
print(max(ac))