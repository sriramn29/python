# n = int(input())
# fact = 1
# for i in range(n):
#     fact = fact * n
#     n = n - 1
# print(fact)

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
num = int(input())
print(factorial(num))