
def Josephus(n, k):
    array = [] # 1부터 n까지의 리스트 생성
    for i in range(n):
        array.append(i + 1)

    result = [] # 제거된 사람들 저장할 리스트

    index = 0 # 시작 인덱스 설정

    # 배열이 빌 때까지 반복
    while len(array) > 0:
        index = index + (k - 1) # k번째 사람을 찾기 위해 (k-1)번의 인덱스 이동

        index = index % len(array) # 모듈러 연산

        removed_value = array.pop(index)
        result.append(removed_value)

    return result

n, k = map(int, input().split())

# 함수 실행 후 결과 저장
result = Josephus(n, k)

# 백준 스타일 출력
print("<" + ", ".join(str(x) for x in result) + ">")

