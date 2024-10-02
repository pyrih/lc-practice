class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)

        next = self.left.next
        prev = self.left

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)

        next = self.right
        prev = self.right.prev

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0:
            node = ListNode(val)
            next = cur
            prev = cur.prev

            prev.next = node
            next.prev = node

            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            next = cur.next
            prev = cur.prev

            next.prev = prev
            prev.next = next
