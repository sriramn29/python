a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
odd = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
print("Evens:", even)
print("Odds:", odd)