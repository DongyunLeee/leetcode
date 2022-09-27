class MyCircularDeque:

    def __init__(self, k: int):
        self.que = [None] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == len(self.que):
            return False

        self.front += len(self.que) - 1
        self.front = self.front % len(self.que)
        self.que[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == len(self.que):
            return False

        self.rear += 1
        self.rear = self.rear % len(self.que)
        self.que[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        self.que[self.front] = None
        self.front += 1
        self.front = self.front % len(self.que)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False

        self.que[self.rear] = None
        self.rear += len(self.que) - 1
        self.rear = self.rear % len(self.que)
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.que[self.front] is None:
            return -1
        else:
            return self.que[self.front]

    def getRear(self) -> int:
        if self.que[self.rear] is None:
            return -1
        else:
            return self.que[self.rear]

    def isEmpty(self) -> bool:
        if self.size == 0:
             return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == len(self.que):
            return True
        else:
            return False