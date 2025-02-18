import random

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head: #head가 none이면 F반환 하는데 not이 있으므로 T반환. 따라서 head가 none이면 if문 실행
            self.head = Node(data)
            return

        current = self.head #current라는 지역변수에 head를 저장.
        while current.next: #current가 가르치고 있는것이 존재하면
            current = current.next

        current.next = Node(data)


    def search(self,target) -> bool:
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False


    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return "end"



if __name__ == "__main__":
    l = LinkedList()
    i = 0
    while i < 20:
        n = random.randint(1,20)
        l.append(n)
        print(n, end = " ")
        i = i + 1
    # print(l)
    print(l.search(10))