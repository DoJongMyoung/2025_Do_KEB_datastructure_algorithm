def bubble_sort(l):
    list_length = len(l) - 1
    for i in range(list_length):
        no_swap = True
        for j in range(list_length - i): # !
            if l[j] > l[j+1]:
                l[j] , l[j + 1] = l[j + 1], l[j]
                no_swap = False
                print(j, end = " ")
        if no_swap:
            return l
    return l

print(bubble_sort([33,8,-11,1]))
print(bubble_sort([11,13,15,19]))