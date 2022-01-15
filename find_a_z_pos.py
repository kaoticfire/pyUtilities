# Method One
def find_a_z_pos_1(arr: list, dest, int):
    for i in range(len(arr)):
        if arr[i] == dest:
            start = arr[i]
            while i + 1 < len(arr) and arr[i+1] == dest:
                i += 1
            return [start, i]
    return [-1, -1]


# Method Two
def find_start_one(arr: list, target: int):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_end_one(arr: list, target: int):
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def find_a_z_pos_2(arr: list, target: int):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start_one(arr, target)
    end = find_end_one(arr, target)
    return [start, end]


# Method Three
def find_a_z_pos_3(arr: list, target: int):
    try:
        start = arr.index(target)
        end = len(arr) - 1 - arr[::-1].index(target)
        return [start, end]
    except ValueError:
        return [-1, -1]


if __name__ == '__main__':
    num_list = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    number = 8
    print(find_a_z_pos_3(num_list, number))
