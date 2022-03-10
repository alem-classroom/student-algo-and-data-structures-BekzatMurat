def binary_search(lst, to_find):
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low+high) // 2
        if lst[mid] == to_find:
            return mid
        elif to_find > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
