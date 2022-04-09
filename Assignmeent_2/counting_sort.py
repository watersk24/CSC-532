import random


def counting_sort(A, B, k):
    k = max(A)
    

    for i in A:
        j = i + 1
        if i <= k:
            C[i] = 0

        # if j <= len(A):
        #     C[A[j]] += 1
        #
        # if A[1] <= k:
        #     C[i] = C[i] + C[i - 1]
        #
        # if
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
