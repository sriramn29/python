def compoundInterest(principle, numberOfYears, rateOfInterest):
    # amount = principle * (pow((1 + rateOfInterest / 100), numberOfYears))
    amount = principle * (1 + (rateOfInterest / 100)) ** numberOfYears
    CI = amount - principle
    print(CI)

principle = float(input())
numberOfYears = float(input())
rateOfInterest = float(input())
compoundInterest(principle, numberOfYears, rateOfInterest)