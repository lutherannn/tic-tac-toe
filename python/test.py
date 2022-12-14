test = ["*", "X", "*", "*", "O", "X", "X", "*", "*"]


def getIndexes(lst, item):
    lstCpy = lst
    r = []
    for x in lst:
        if x == item:
            r.append(lst.index(x))
            lstCpy[lstCpy.index(x)] = "A"
    return r


print(getIndexes(test, "*"))
