ThisDict = {
    "Name": "Sriram",
    "Department": "ECE",
    "Rollno": 204
}
for x in ThisDict:
    print(x)

for x in ThisDict:
    print(ThisDict[x])

for x in ThisDict.values():
    print(x)

#loop through both keys and values, by using the items() function
for x, y in ThisDict.items():
    print(x, y)