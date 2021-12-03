f = open('input.txt', 'r')

values = f.read().split('\n')

resultOxy = []
resultCo2 = []

def filterList(list, base) -> list:
    result = []
    for i in list:
        if i.startswith(base):
            result.append(i)
    return result

def searchOxy(list, x, base) -> list:
    tmp0 = 0
    tmp1 = 0

    for i in list:
        if i[x] == '0':
            tmp0 += 1
        else:
            tmp1 += 1

    if tmp1 > tmp0 or tmp1 == tmp0:
        base += '1'
        list = filterList(list, base)
    else:
        base += '0'
        list = filterList(list, base)
    if len(list) == 1:
        return list
    return searchOxy(list, x + 1, base)

def searchCo2(list, x, base) -> list:
    tmp0 = 0
    tmp1 = 0

    for i in list:
        if i[x] == '0':
            tmp0 += 1
        else:
            tmp1 += 1

    if tmp1 > tmp0 or tmp1 == tmp0:
        base += '0'
        list = filterList(list, base)
    else:
        base += '1'
        list = filterList(list, base)
    if len(list) == 1:
        return list
    return searchCo2(list, x + 1, base)

resultOxy = int(searchOxy(values, 0, "")[0], 2)
resultCo2 = int(searchCo2(values, 0, "")[0], 2)

print(resultOxy * resultCo2)