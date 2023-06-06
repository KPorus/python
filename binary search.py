data = [13, 11, 10, 7, 4, 3, 1, 0]

def binary_search(data, key):
    start = 0
    end = len(data) - 1
    if len(data) > 0:
        while start <= end:
            mid = (start + end) // 2

            if data[mid] < key:
                start = mid + 1
            elif data[mid] > key:
                end = mid - 1
            else:
                return mid
        return -1
    return -1

result = binary_search(data, 7)
print(result)
