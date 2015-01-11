def mergesort(items):
    if len(items) > 1:

        mid = len(items) / 2    # dividing point
        left = items[0:mid]     #left array
        right = items[mid:]     #right array

        mergesort(left)            # for subdivisions of left array
        mergesort(right)           # for subdivisions of right array

        l, r = 0, 0
        for i in range(len(items)):     # Merging the left and right list

            if l < len(left):
                 lval = left[l]
            else: None
            rval = right[r] if r < len(right) else None

            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1            
    return items
