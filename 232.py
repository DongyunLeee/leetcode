# 파이썬은 스택자료형이 없어 리스트 자료형으로 스택을 구현하여 문제풀이 진행
class MyQueue:

    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.pop(0))

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) > 0:
            return False
        else:
            return True
