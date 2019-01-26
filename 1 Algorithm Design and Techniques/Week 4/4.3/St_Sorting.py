# Uses python3
import sys
import random


def partition3(A, LEFT, RIGHT):
    DM_val = A[LEFT]
    DM_lft = i = LEFT
    DM_RGT = RIGHT
    while i <= DM_RGT:
        if A[i] < DM_val:
            A[i], A[DM_lft] = A[DM_lft], A[i]
            DM_lft = DM_lft + 1
            i = i + 1
        elif A[i] == DM_val:
            i = i + 1
        else:
            A[i], A[DM_RGT] = A[DM_RGT], A[i]
            DM_RGT -= 1
        Indx = [DM_lft, DM_RGT]
    return Indx


def partition2(A, LEFT, RIGHT):
    pivot = random.randint(LEFT, RIGHT)
    A[RIGHT], A[pivot] = A[pivot], A[RIGHT]
    DM_val = A[RIGHT]
    pIndex = LEFT
    for i in range(LEFT, RIGHT):
        if A[i] <= DM_val:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1
    A[RIGHT], A[pIndex] = A[pIndex], A[RIGHT]
    return pIndex


def randomized_quick_sort(A, LEFT, RIGHT):
    if LEFT >= RIGHT:
        return

    pivot = random.randint(LEFT, RIGHT)
    A[LEFT], A[pivot] = A[pivot], A[LEFT]
    pIndex = partition3(A, LEFT, RIGHT)
    randomized_quick_sort(A, LEFT, pIndex[0] - 1)
    randomized_quick_sort(A, pIndex[1] + 1, RIGHT)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    randomized_quick_sort(A, 0, n - 1)
    for x in A:
        print(x, end=' ')
