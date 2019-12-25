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

def remove_min(L):
    # your code here
    L[0] = L.pop()
    down_heapify(L, 0)
    return L

def up_heapify(L, i):
    print i

    if min(L[left(i)], L[right(i)]) >= L[i]: return

    if L[i] > L[left(i)]:
        (L[i], L[left(i)]) = (L[left(i)], L[i])
        if not root(i): up_heapify(L, parent(i))
        return

    (L[i], L[right(i)]) = (L[right(i)], L[i])
    if not root(i): up_heapify(L, parent(i))
    return

def insert(L, value):
    L.append(value)
    up_heapify(L, parent(len(L)-1))

# build_heap
def build_heap(L):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
    return L
def check_heap(L):
    # check whether L is a right HEAP
    return sum(check_node(L, i) for i in range(0, len(L)>>1)) == len(L)>>1
def check_node(L, i):
    return 1 if min(L[left(i)], L[right(i)]) >= L[i] else 0

def test():
    L = [84, 20, 48, 49, 59, 44, 21, 80, 51, 59, 60, 96, 66, 71, 69, 30, 10, 86, 49, 91]
    print L
    build_heap(L)
    print L
    insert(L, 1)
    print L
    assert check_heap(L), 'L must be right heap'