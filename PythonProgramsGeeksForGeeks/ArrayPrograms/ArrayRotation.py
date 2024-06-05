def rotateLeft(a, n):
    return a[n:] + a[0:n]
def rotateRight(a, n):
    return a[len(a) - n:] + a[0:len(a) - n]
a = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]
numberOfRotation = int(input("Enter the numnber of rotations : "))
leftOrRightRotation = input("Enter Whether to rotate left or right (Left/Right) : ")
if(leftOrRightRotation == "Left"):
    print(rotateLeft (a, numberOfRotation))
elif(leftOrRightRotation == "Right"):
    print(rotateRight(a, numberOfRotation))