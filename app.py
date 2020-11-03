# liner search 
def liner_search(list, target):
    for i in list:
        if i == target:
            return True
    return False

list = [1,2,3,4,5]
target = 6

print(liner_search(list, target))