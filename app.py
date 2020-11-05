# liner search 
def liner_search(list, target):
    for i in list:
        if i == target:
            return True
    return False

# iterative binary search

def iterative_search(list, target):
    low = 0
    high = len(list) - 1
    while high >= low:
        mid = (low + high ) //2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            low = mid +1
        else :
            high = mid -1

    return False

# recursive binary search
def recursive_search(list, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            return recursive_search(list, target, mid+1, high)
        else:
            return recursive_search(list, target, low, mid-1)


list = [1,2,3,4,5,6]
target = 1

print(recursive_search(list, target, 0, len(list)-1))

