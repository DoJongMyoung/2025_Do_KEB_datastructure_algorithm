def is_even(number):
    """
    짝수 판정 함수
    :param number: 판정할 함수
    :return: 짝수면 True, 홀수면 False
    """
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input())

print(is_even(number))