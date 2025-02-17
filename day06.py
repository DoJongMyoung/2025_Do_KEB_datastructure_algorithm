def is_even(number):
    """
    짝수 판정 함수
    :param number: 판정할 함수
    :return: 짝수면 True, 홀수면 False
    """

    return not number & 1
    #return number & 1 # 짝수 넣으면 0반환 홀수 넣으면 1반환


num = int(input())

print(is_even(num))
