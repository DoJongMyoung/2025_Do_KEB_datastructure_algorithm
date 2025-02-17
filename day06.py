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

num = int(input())

print(is_even(num))

#bit operation

a = 10 # 0000 1010
b = 11 # 0000 1011

print(a & b) # 0000 1010 <- &연산은 둘다 1일때만 1 나머지 경우엔 전부 0
print(a | b) # 0000 1011 <- | 하나라도 1이면 1
print(a ^ b) #0000 0001 <- ^는 값이 서로 다를때 1 아니면 0