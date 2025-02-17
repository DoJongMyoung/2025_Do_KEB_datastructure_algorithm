#숫자를 입력했을때 8진수 결과를 내어놓는 프로그램 작성하기

def dec_oct(n):
    if n == 0:
        return ""
    else:
        return dec_oct(n // 8) + str(n % 8) # //는 몫을 나타냄. %는 나머지

n = int(input())
print(dec_oct(n))


# def is_even(number):
#     """
#     짝수 판정 함수
#     :param number: 판정할 함수
#     :return: 짝수면 True, 홀수면 False
#     """
#
#     return not number & 1
#     #return number & 1 # 짝수 넣으면 0반환 홀수 넣으면 1반환
#
#
# num = int(input())
#
# print(is_even(num))
#
