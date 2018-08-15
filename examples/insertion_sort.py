def insertion_sort(l):
    lst = list(l)
    for i in range(len(lst)):
        for j in range(i, 0, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
            else:
                break
    return lst