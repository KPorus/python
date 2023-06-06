from math import ceil

data = [1,2,3,4,5,6,7,8,9]

def binary_search(data, key):
    start = 0
    end = len(data) - 1
    if len(data)>0:
        while start <= end:
            mid = ceil((start + end) / 2)

            if data[mid] < key:
                start = mid + 1
            elif data[mid] > key:
                end = mid - 1
            else:
                return mid

        return -1
    return -1

result = binary_search(data, 12)
print(result)
