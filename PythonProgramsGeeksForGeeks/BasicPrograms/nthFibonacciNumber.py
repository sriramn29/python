number = int(input())
a = 0
b = 1
if number == 0:
    print(a)
elif number == 1:
    print(b)
else:
    for i in range(2, number):
        c = a + b
        a = b
        b = c
        print(b)