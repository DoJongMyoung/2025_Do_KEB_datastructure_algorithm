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

students = []

try:
    file = input("File name : ")
    fp = open(file, 'r')
    readme_list = fp.readlines()
    rls = readme_list[0].split("_")
    print(readme_list)
    print(rls)
    fp.close()

except FileNotFoundError as err: #여기서 err은 에러 메세지를 받는 변수명 , 다른거 써도 무관
    print(f"{file} is not exist . {err}")