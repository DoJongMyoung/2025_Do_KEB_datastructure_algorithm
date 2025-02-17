def sum(num):
    #O(n) 시간복잡도  on
    sum_num = 0
    for i in range(1, num+1 ,1):
        sum_num = sum_num + i

    return sum_num


n = int(input())
print(sum(n))
