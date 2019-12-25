#import random
#L = [random.randrange(90) + 10 for i in range(20)]
L = [84, 20, 48, 49, 59, 44, 21, 80, 51, 59, 60, 96, 66, 71, 69, 30, 10, 86, 49, 91]

# Heap basic functions
def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)/2
def root(i): return i == 0
def leaf(L, i): return left(i) >= len(L) and right(i) >= len(L)
def one_child(L, i): return right(i) == len(L)

def down_heapify(L, i):
    if leaf(L, i): return

    if one_child(L, i):
        if L[i] > L[left(i)]:
            (L[i], L[left(i)]) = (L[left(i)], L[i])
        return

    if min(L[left(i)], L[right(i)]) >= L[i]: return

    if L[left(i)] < L[right(i)]:
        (L[i], L[left(i)]) = (L[left(i)], L[i])
        down_heapify(L, left(i))
        return
    (L[i], L[right(i)]) = (L[right(i)], L[i])
    down_heapify(L, right(i))
    return