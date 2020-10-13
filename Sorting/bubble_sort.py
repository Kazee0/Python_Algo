def bubble_sort( list1 ):
    n = len(list1)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1
