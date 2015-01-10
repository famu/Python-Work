#inversions counting using mergsort
inversion = 0

def merge (left,right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.remove(left[0])
            else:
                global inversion
                inversion += len(left)
                result.append(right[0])
                right.remove(right[0])
        elif len(left) > 0:
            result += left
            left = []
        elif len(right) > 0:
            result += right
            right = []
    return result


def inversions(list):
    size = len(list)
    if size <= 1:
        return list #consider it sorted
    mid = int(size / 2)
    left = list[:mid]
    right = list[mid:]
    left = inversions(left)
    right = inversions(right)
    return merge(left,right)



inversions([3,1,4,2])
print(inversion)
