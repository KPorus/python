# data = [13, 11, 10, 7, 4, 3, 1, 0]
# data = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
data = [8, 8, 7, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]

def find_loaction(data,mid,key):
    mid_value = data[mid]
    print("mid:", mid,"mid_value:", mid_value,"value:" ,data[mid],"key:",key)
    if mid_value == key:
        if mid - 1 >= 0 and data[mid - 1] == key:
            return 'left'
        else:
            return 'found'
    elif mid_value < key:
        return 'left'
    else:
        return 'right'
def binary_search(data, key):
    start = 0
    end = len(data) - 1
    if len(data) > 0:
        while start <= end:
            mid = (start + end) // 2
            result = find_loaction(data,mid,key)
            if result == "right":
                start = mid + 1
            elif result == "left":
                end = mid - 1
            else:
                return mid
        return -1
    return -1

result = binary_search(data, 7)
print(result)
