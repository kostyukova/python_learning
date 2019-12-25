#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#
import random

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos


def partition(L, v):
    left = []
    right = []
    for val in L:
        if val < v:
            left.append(val)
        if val > v:
            right.append(val)
    return (left, [v], right)

def top_k(L, k):
    v = L[random.randrange(len(L))]
    (left, middle, right) = partition(L, v)
    if len(left) == k: return left
    if len(left) + 1 == k: return left + middle
    if len(left) > k: return top_k(left, k)
    return left + middle + top_k(right, k - len(left) - 1)

def test_partition():
    L=[3, 7, 22, 6, 9, 57, 75, 32, 66, 45]
    P = partition(L, L[len(L)/2])
    print P

def test_top_k():
    L=[3, 7, 22, 6, 9, 57, 75, 32, 66, 45]
    print top_k(L, 7)

test_top_k()