start = int(input())
end = int(input())
a = [-10, -8, -6, -4, -2, 0, 1, 3, 5, 7, 9]
positive = []
negative = []
for i in range(start, end):
    if a[i] < 0:
        negative.append(a[i])
    else:
        positive.append(a[i])
print("Positives:", positive)
print("Negatives:", negative)