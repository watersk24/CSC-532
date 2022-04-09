import random
import time
import pandas as pd
import matplotlib.pyplot as plt

def quicksort(A):
    quicksortHelper(A, 0, len(A) - 1)


def quicksortHelper(A, first, last):
    if first < last:
        splitpoint = partition(A, first, last)

        quicksortHelper(A, first, splitpoint - 1)
        quicksortHelper(A, splitpoint + 1, last)


def partition(A, first, last):
    pivotvalue = A[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and A[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while A[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            A[leftmark], A[rightmark] = A[rightmark], A[leftmark]

    A[first], A[rightmark] = A[rightmark], A[first]
    return rightmark


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


# Driver Code
num = 20
start = 1
end = 50
A = Rand(start, end, num)


l = []

for i in range(1, 21):
    start = time.time_ns()
    quicksort(A)
    stop = time.time_ns()
    elapsed_runtime = stop - start
    l.append(elapsed_runtime)
    time.sleep(2)

df = pd.DataFrame(l)
print(df)
# plt.plot(l)
# plt.scatter(len(l), l)
# plt.savefig("runtime")
#
# df.to_excel('quicksort_runtimes.xlsx')
# sum_of_times = sum(l)
# avg = sum_of_times / len(l)
# print("Elapsed runtime: ", l)
# print("Mean runtime: ", avg)
#plt.show()
