def bubble_sort(l):
    list_length = len(l) - 1
    for i in range(list_length):
        for j in range(list_length):
            if l[j] > l[j+1]:
                l[j] , l[j + 1] = l[j + 1], l[j]
    return l

print(bubble_sort([7,-11,66,4]))