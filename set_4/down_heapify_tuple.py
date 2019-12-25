
# Heap basic functions
def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)/2
def root(i): return i == 0
def leaf(L, i): return left(i) >= len(L) and right(i) >= len(L)
def one_child(L, i): return right(i) == len(L)

def down_heapify(L, i, func):
    if leaf(L, i): return

    if one_child(L, i):
        if func(L[i]) > func(L[left(i)]):
            (L[i], L[left(i)]) = (L[left(i)], L[i])
        return

    if min(func(L[left(i)]), func(L[right(i)])) >= func(L[i]): return

    if func(L[left(i)]) < func(L[right(i)]):
        (L[i], L[left(i)]) = (L[left(i)], L[i])
        down_heapify(L, left(i), func)
        return
    (L[i], L[right(i)]) = (L[right(i)], L[i])
    down_heapify(L, right(i), func)
    return

# build_heap
def build_heap(L, func):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i, func)
    return L

def push_min(L, value, func):
    L[0] = value
    down_heapify(L, 0, func)