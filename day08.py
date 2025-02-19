# 이진 탐색 트리(BST) 삽입, 검색, 삭제 함수를 설계하고 코드로 작성하시오.
# 삭제 함수에는 리프(LEAF) 노드, 자식이 1개인 경우 그리고 자식이 2개인 경우를 고려하시오.


class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def search(root, find_group):  # 검색함수.
    current = root  # 루트에서 시작
    while True:
        if find_group == current.data:  # 값이 일치하면 찾았다고 출력
            print(f"{find_group}을(를) 찾았습니다")
            break

        elif find_group < current.data:  # 찾을 값이 현재 값보다 작으면 왼쪽 이동
            if current.left is None:  # 왼쪽이 없으면 트리에 없음
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.left  # 왼쪽으로 이동

        else:  # 찾을 값이 현재 값보다 크면 오른쪽 이동
            if current.right is None:  # 오른쪽이 없으면 트리에 없음
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.right  # 오른쪽으로 이동


def insert(root, data):  # 삽입 함수. <- 넣을 data와 특정 데이터 하나를 비교해서 작으면 왼쪽으로 크면 오른쪽으로 이동시켜서 저장.
    node = TreeNode()
    node.data = data

    if root is None:  # 노드가 비어있을때
        return node

    current = root  # 주소값 전달
    while True:
        if data == current.data:  # 추가할 데이터가 있으면 함수 종료.
            print(f"{data}가 이미 존재하므로 추가 하지 않습니다.")
            return root

        if str(data) < str(current.data):  # 문자열을 입력받았을때 오류가 나지 않게 문자열로 바꾸어서 비교
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

    return root


def delete(root, data):
    if root is None:  # 트리가 비어있는경우
        return root

    if data < root.data:
        root.left = delete(root.left, data)  # 왼쪽 노드로 이동
    elif data > root.data:
        root.right = delete(root.right, data)  # 오른쪽 노드로 이동

    else:
        # 자식이 하나일때
        if root.left is None and root.right is None:  # 왼쪽 오른쪽노드가 다 비어있는 경우
            return  # 반환값 없음
        elif root.left is None:  # 오른쪽 노드만 존재할 경우
            return root.right  # 오른쪽 자식이 부모와 연결되도록 반환
        elif root.right is None:  # 왼쪽 자식만 존재할 경우
            return root.left  # 왼쪽 자식이 부모와 연결되도록 반환

        else:
            min_node = find_min(root.right)  # 오른쪽 서브트리에서 가장 작은 값 찾기

            root.data = min_node.data  # 현재 노드의 데이터를 최소값으로 교체

            root.right = delete(root.right, min_node.data)  # 최소값을 삭제함

    return root


def find_min(node):  # 오른쪽 서브트리에서 가장 작은 값(삭제하려는 녀석보다 큰 놈들 중에서 가장 작은 녀석)을 찾는 함수 , 정렬을 깨지 않기 위해 필요함.

    current = node

    while current.left is not None:
        current = current.left

    return current


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end='-')
    in_order(node.right)


def tree(groups, root):  # 트리 생성
    for value in groups[1:]:
        root = insert(root, value)
    return root


if __name__ == "__main__":
    groups = [20, 70, 80, 90, 50, 10, 30, 75]
    root = None

    root = tree(groups, root)

    print("BST 구성 완료")

    print("초기 트리 상태 (삽입 후)")
    in_order(root)
    print()

    root = delete(root, 30)
    print("트리 상태 (30 삭제 후)")
    in_order(root)
    print()

    root = delete(root, 50)
    print("트리 상태 (50 삭제 후)")
    in_order(root)
    print()

    root = delete(root, 70)
    print("트리 상태 (70 삭제 후)")
    in_order(root)
    print()