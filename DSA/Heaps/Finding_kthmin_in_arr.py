class MinHeap:

    def __init__(self, a, size):

        self.harr = a

        self.capacity = None

        self.heap_size = size

        i = int((self.heap_size - 1) / 2)
        while i >= 0:
            self.minHeapify(i)
            i -= 1

    def parent(self, i):
        return (i - 1) / 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def getMin(self):
        return self.harr[0]

    def extractMin(self):
        if self.heap_size == 0:
            return float("inf")

        root = self.harr[0]

        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.minHeapify(0)
        self.heap_size -= 1
        return root

    def minHeapify(self, i):
        ui=self.harr
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if ((l < self.heap_size) and
                (self.harr[l] < self.harr[i])):
            smallest = l
        if ((r < self.heap_size) and
                (self.harr[r] < self.harr[smallest])):
            smallest = r
        if smallest != i:
            self.harr[i], self.harr[smallest] = (
                self.harr[smallest], self.harr[i])
            self.minHeapify(smallest)

def kthSmallest(arr, n, k):
    mh = MinHeap(arr, n)
    for i in range(k - 1):
        mh.extractMin()
    return mh.getMin()


arr = [12, 3, 5, 7, 19]
n = len(arr)
k = 2
print("K'th smallest element is", kthSmallest(arr, n, k))

