
class MinHeap:

    def __init__(self):
        self.list = [0]
        self.size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.list[i] < self.list[i // 2]:
                tmp = self.list[i // 2]
                self.list[i // 2] = self.list[i]
                self.list[i] = tmp
            i = i // 2

    def insert(self, item):
        self.list.append(item)
        self.size = self.size + 1
        self.percolate_up(self.size)

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            if self.list[i] > self.list[mc]:
                tmp = self.list[i]
                self.list[i] = self.list[mc]
                self.list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.list[i * 2] < self.list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def remove(self):
        retval = self.list[1]
        self.list[1] = self.list[self.size]
        self.size = self.size - 1
        self.list.pop()
        self.percolate_down(1)
        return retval

    def build_heap(self, lst):
        i = len(lst) // 2
        self.size = len(lst)
        self.list = [0] + lst[:]
        while i > 0:
            self.percolate_down(i)
            i = i - 1


if __name__ == "__main__":

    h = MinHeap()
    h.build_heap([3, 2, 18, 4, 22, 3, 3, 12, 4])
    assert h.size == 9
    h.remove()
    h.remove()
    h.remove()
    h.remove()
    h.remove()
    h.remove()
    h.remove()
    h.remove()
    h.remove()
    assert h.size == 0

    h = MinHeap()
    h.insert(5)
    h.insert(1)
    assert h.size == 2
    assert h.remove() == 1
