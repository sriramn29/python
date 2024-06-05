number = int(input())
copy = number
lenght = len(str(number))
a = 0
while number != 0:
    r = number % 10
    a = a + (r**lenght)
    number = number // 10
print("yes" if copy == a else "No")