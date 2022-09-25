from queue import Queue


# Queue를 사용하여 Stack 구현
class MyStack:

    def __init__(self):
        self.object = Queue()

    def push(self, x: int) -> None:
        self.object.put(x)

    def pop(self) -> int:
        for i in range(self.object.qsize() - 1):
            self.object.put(self.object.get())
        return self.object.get()

    def top(self) -> int:
        for i in range(self.object.qsize() - 1):
            self.object.put(self.object.get())
        ret = self.object.get()
        self.object.put(ret)
        return ret

    def empty(self) -> bool:
        return self.object.empty()


# List를 이용한 Stack 구현
# class MyStack:
#
#     def __init__(self):
#         self.object = list()
#
#     def push(self, x: int) -> None:
#         self.object.append(x)
#
#     def pop(self) -> int:
#         return self.object.pop()
#
#     def top(self) -> int:
#         if len(self.object) > 0: return self.object[-1]
#
#     def empty(self) -> bool:
#         if len(self.object) > 0:
#             return False
#         else:
#             return True
