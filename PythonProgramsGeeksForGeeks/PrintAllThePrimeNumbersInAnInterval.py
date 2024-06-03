def PrimeNumbers(startOfNumber, EndOfNumber):
    prime = []
    for i in range(startOfNumber,EndOfNumber):
            for j in range(2,int(i/2)+1):
                if i % j == 0:
                    break
                else:
                    prime.append(i)
    print(prime)

startOfNumber = int(input())
EndOfNumber = int(input())
PrimeNumbers(startOfNumber, EndOfNumber)