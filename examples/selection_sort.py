from operator import itemgetter

def selection_sort(l):
    lst = list(l)
    for i in range(len(lst)):
        j, _ = min(enumerate(lst[i:]), key=itemgetter(1))
        lst[i], lst[i+j] = lst[i+j], lst[i]
    return lst