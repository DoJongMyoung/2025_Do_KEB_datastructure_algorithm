#Assignment
# v4.4) v4.3 버전의 출력방식을 너비 우선 탐색으로 수정하시오 .
from collections import deque


class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


def insert(root, value):
    if root is None:
        node = TreeNode()
        node.data = value
        return node

    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def search(root, value):
    current = root
    while current:
        if value == current.data:
            return current
        elif value < current.data:
            current = current.left
        else:
            current = current.right
    return None


# def post_order(node):
#     if node is None:
#         return
#     post_order(node.left)
#     post_order(node.right)
#     print(f"{node.data} ", end='')

def bfs(root):
	if root is None: #노드가 비어있으면 함수 종료
		return

	#노드가 비어 있지 않은 경우
	# print([root]) <- [root]형태로 쓰면 iterable한 형태로 root 주소를 queue에 저장 할 수 있음
	queue = deque([root])  # 시작 노드를 큐에 추가
	while queue:
		node = queue.popleft()  # 큐에서 노드를 꺼냄
		print(f"{node.data} ", end="")  # 현재 노드 출력

		if node.left:
			queue.append(node.left)  # 왼쪽 자식 노드가 있으면 큐에 추가
		if node.right:
			queue.append(node.right)  # 오른쪽 자식 노드가 있으면 큐에 추가

def delete(root, value):
    if root is None:
        return root
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:  # 자식이 두 개인 경우
            root.data = find_min(root.right).data
            root.right = delete(root.right, root.data)
    return root


def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number)

    while True:
        print("\n--- 트리 관리 메뉴 ---")
        print("1. 값 삽입")
        print("2. 값 삭제")
        print("3. 값 찾기")
        print("4. 트리 확인 (너비 우선 탐색)")
        print("5. 종료")
        choice = input("원하는 작업을 선택하세요: ")
        if choice == '1':
            value = int(input("삽입할 값을 입력하세요: "))
            root = insert(root, value)
            print(f"{value} 삽입 완료")
        elif choice == '2':
            value = int(input("삭제할 값을 입력하세요: "))
            if search(root, value):
                root = delete(root, value)
                print(f"{value} 삭제 완료")
            else:
                print(f"{value}은(는) 트리에 존재하지 않습니다.")
        elif choice == '3':
            value = int(input("찾고 싶은 값을 입력하세요: "))
            if search(root, value):
                print(f"{value}을(를) 찾았습니다.")
            else:
                print(f"{value}이(가) 존재하지 않습니다.")
        elif choice == '4':
            bfs(root)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")