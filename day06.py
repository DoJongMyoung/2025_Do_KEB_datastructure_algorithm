# list = [20,30,40,40,50,80,80,80,90]
#
# print(list)
#
# list.pop(4)
#
# print(list)
#
# list.remove(80)
#
# print(list)

import csv
import random

students = []

try:
    with open("students.csv", 'r') as fp:
        students_list = fp.readlines()
        print(students_list)
        students_list.remove("이상혁\n")
        students_list.remove("김찬빈\n")
        students_list.remove("김철중\n")

        for _ in range(3):
            random_pick = random.choice(students_list)
            print(random_pick,end='')
            students_list.remove(random_pick)

except FileNotFoundError as err: #여기서 err은 에러 메세지를 받는 변수명 , 다른거 써도 무관
    print(err)