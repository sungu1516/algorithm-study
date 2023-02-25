# 재귀
def binary_search(arr,target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, end - 1)
    else:
        return binary_search(arr, target, start + 1, end)

# 반복문
def bin_search(arr,target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end -= 1
        else:
            start += 1

    return None

test_arr = [0, 1, 3, 5, 7]
print(bin_search(test_arr, 7, 0, len(test_arr) - 1))