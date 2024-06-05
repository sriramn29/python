def isMonotonic(a):
    return (all(a[i] >= a[i + 1] for i in range(len(a) - 1)) or all(a[i] <= a[i + 1] for i in range(len(a) - 1)))
a = [1, 2, 3, 2, 5, 6, 7, 8, 9]
print(isMonotonic(a))