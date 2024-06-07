def swaplist(list):
    # start, *middle, end  = list
    # list = [end, *middle, start]
    list[0], list[len(a)-1] = list[len(a)-1], list[0]
    return list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(swaplist(a))