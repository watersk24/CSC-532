# Student names: Kevin Waters

# Assume that Dr. Song is broadcasting his Algorithm lectures on Twitch and there are 1000 people watching.
# Some of the audiences are generous enough and they want to tip Dr. Song.  ;-)
# Dr. Song wants to design a graphic interface that always shows the top N highest tip amounts.
# Especially, he always wants to show the nth highest tip amount on the screen like:
# "If you sent a tip higher than ***, you will receive a RaspBerry Pi for free." (*** is the nth highest tip)
# Please design a data structure (a fixed-length priority queue) which records the top n tip amounts on the fly.
# When a new tip comes, the processing/updating time should be faster than Theta(n).
# Accessing the nth largest tip amount should be **constant**.
# The data structure should take Theta(n) memory space, which means we cannot save all the
# tip amounts in a large list.

# Hint: below is an implementation of MinHeap in Python, you should create a class "NthHighestTipper" that has a
# MinHeap object. You should not modify the code of this MinHeap class.
# The "NthHighestTipper" class should have the methods below:
#    - constructor, takes the parameter n (in the example below, n=5)
#    - incomingTip, takes a parameter amount. It prints "Thank you for tipping $**", updates the priority queue
#       if the tip is higher than the current nth highest.
#       It also prints "If you sent a tip higher than ***  you will receive a RaspBerry Pi for free." when the priority
#       queue is updated.
#    - peak, returns the current nth highest tip. It does not change the priority queue.
# The "If you sent a tip higher than ***, you will receive a RaspBerry Pi for free." only starts to appear after the
# priority queue is full and the incoming tip is higher than the nth highest.


class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def heapify(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.heapify(1)
        return retval

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def peak(self):
        if self.currentSize == 0:
            return None
        return self.heapList[1]


class NthHighestTipper:
    def __init__(self, n):
        self.max_size = n
        self.heap = MinHeap()

    def incomingTip(self, amount):
        print(f"Thank you for tipping: ${amount}")
        heap = self.heap

        # build initial heap
        if heap.currentSize < self.max_size:
            heap.insert(amount)

        #  update priority queue with tip amount if it is greater than nth highest tip
        elif amount > self.peak() and heap.currentSize == self.max_size:
            heap.delMin()
            heap.insert(amount)
            print(f"If you tip higher than ${heap.heapList[1]} you can receive a free Raspberry Pi")

    def peak(self):
        #  return Nth highest tip, look in priority queue for N
        m = self.heap.heapList[-1]
        return m

# Code for testing, do not change
dr_song_top_5_highest_tipper = NthHighestTipper(5)
dr_song_top_5_highest_tipper.incomingTip(5)
dr_song_top_5_highest_tipper.incomingTip(6)
dr_song_top_5_highest_tipper.incomingTip(3)
dr_song_top_5_highest_tipper.incomingTip(4)
dr_song_top_5_highest_tipper.incomingTip(7)
dr_song_top_5_highest_tipper.incomingTip(8)
dr_song_top_5_highest_tipper.incomingTip(18)
dr_song_top_5_highest_tipper.incomingTip(28)
dr_song_top_5_highest_tipper.incomingTip(2)
dr_song_top_5_highest_tipper.incomingTip(38)

print("current number", dr_song_top_5_highest_tipper.max_size, "highest tip is:", dr_song_top_5_highest_tipper.peak())

# expected output:
"""
Thank you for tipping $ 5
Thank you for tipping $ 6
Thank you for tipping $ 3
Thank you for tipping $ 4
Thank you for tipping $ 7
Thank you for tipping $ 8
if you tip higher than 4  you can receive a free Raspberry Pi
Thank you for tipping $ 18
if you tip higher than 5  you can receive a free Raspberry Pi
Thank you for tipping $ 28
if you tip higher than 6  you can receive a free Raspberry Pi
Thank you for tipping $ 2
Thank you for tipping $ 38
if you tip higher than 7  you can receive a free Raspberry Pi
current number 5 highest tip is: 7
"""