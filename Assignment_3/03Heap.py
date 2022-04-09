# Student name(s): Kevin Waters
# Please finish this Binary Heap class based on the pseudocode on the textbook (section 6.2-6.4 in textbook).
# You are expected to finish the heapify method and the heapSort method
# You code should generate the expected output.

# Please note that, the first item in the list is a 0, and this value is not used in the heap.
# By adding this 0, we can start the maximum value in the heap at index 1.

# When printing the sorted list, it is okay that the sorted list starts with an extra 0.
# The grading will be done using the provided test case, plus additional ones.

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def heapify(self, i):
        A = self.heapList
        left = self.left(i) # left child
        right = self.right(i) # right child
        parent = self.parent(i)

        if (left <= len(A)) and (A[left] > A[parent]): #value at A[left] > A[i]
            largest = left
        else:
            largest = parent

        if (right <= len(A)-1) and A[right] > A[largest]:
            largest = right

        if largest != parent:
            A[largest], A[parent] = A[parent], A[largest]
            self.heapify(A[largest])

    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.heapify(1)
        return retval

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        i = len(alist) // 2
        while (i > 0):
            self.heapify(i)
            i = i - 1

    def parent(self, i):
        return i//2

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i + 1

    def heapSort(self):
        A = self.heapList
        self.buildHeap(A)
        for i in range(len(A), A[2]):
            A[1], A[i] = A[i], A[1]
            self.currentSize = self.currentSize - 1
            self.heapify(A[1])
        return A

# Code for testing, do not change
my_heap = BinHeap()
my_heap.buildHeap([0, 10, 5, 2, 7,11,6])

print("the current heap has the the values:", my_heap.heapList)

print(my_heap.delMax(), "deleted")

print("the current heap has the the values:", my_heap.heapList)

my_heap.heapSort()

print("sorted:", my_heap.heapSort())

# expected output:
# the current heap has the the values: [0, 11, 10, 6, 2, 7, 5, 0]
# 11 deleted
# the current heap has the the values: [0, 10, 7, 6, 2, 0, 5]
# sorted: [0, 0, 2, 5, 6, 7, 10]