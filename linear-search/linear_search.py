def linear_search(lst, to_find):
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1
    len_lst = len(lst)
    for i in range(len_lst):
        if lst[i] == to_find:
            return i

    return -1


print(linear_search([1, 2, 3, 4], 4))
