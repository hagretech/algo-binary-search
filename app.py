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
list = [1,2,3,4,5]
target = 6

print(iterative_search(list, target))

