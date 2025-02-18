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


if __name__ == "main":
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)
