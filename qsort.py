def qsort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot ]
        right = [x for x in a[1:] if x >= pivot]
        return [qsort(left)] + [pivot] + [qsort(right)]
