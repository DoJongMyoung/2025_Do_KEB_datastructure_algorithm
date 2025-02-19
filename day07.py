#for문을 사용함으로써 시간 복잡도가 O(n)이 되어버린 문제 고쳐보기.
#원형 링크드 리스트 <- 지하철 2호선
#공간을 하나 사용하게 됨.

def is_queue_full() :
    global size, queue, front, rear
    if (rear + 1) % size == front: # 가득찬 상태와 비어있는 상태를 구분하기 위해 메모리를 조금 손해보고 이런 조건을 사용함.
        return True
    else:
        return False

def is_queue_empty() :
    if front == rear:
        return True
    else :
        return False

def en_queue(data) :
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % size
    queue[rear] = data

def de_queue() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % size]

size = int(input("큐의 크기를 입력 : "))
queue = [None for _ in range(size)]
front = rear = 0 # 모듈러 연산을 위해 0으로 시작하는게 바람직함.

if __name__ == "__main__" :
    while True:
        menu = input("삽입(E)/삭제(D)/확인(P)/종료(X) : ")
        if menu == 'X' or menu == 'x':
            break
        elif menu== 'E' or menu == 'e' :
            data = input("입력할 데이터 : ")
            en_queue(data)
            print(queue)
        elif menu== 'D' or menu == 'd' :
            print("삭제된 데이터 : ", de_queue())
            print(queue)
        elif menu== 'P' or menu == 'p' :
            print("확인된 데이터 : ", peek())
            print(queue)
        else:
            print("입력이 잘못됨")
    print("프로그램 종료!")