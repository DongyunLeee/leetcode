# Python은 보통 해시맵 구현에 딕셔너리 자료형을 이용함
class MyHashMap:

    def __init__(self):
        self.hash = {}

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value

    def get(self, key: int) -> int:
        return self.hash.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.hash:
            del self.hash[key]
