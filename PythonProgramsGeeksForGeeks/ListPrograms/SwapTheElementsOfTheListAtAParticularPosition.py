def swaplist(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pos1, pos2 = 1, 3
print(swaplist(a, pos1, pos2))