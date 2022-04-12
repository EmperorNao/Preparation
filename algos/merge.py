

def merge(a, l, r, b, q, p, inplace, start):

    c = [0] * (r - l + 1 + p - q + 1)
    i = l
    j = q
    k = 0
    while i <= r and j <= p:

        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1

        k += 1

    while i <= r:
        c[k] = a[i]
        k += 1
        i += 1

    while j <= p:
        c[k] = b[j]
        k += 1
        j += 1

    for k in range(r - l + 1 + p - q + 1):
        inplace[start + k] = c[k]



def mergesort(a, l, r):
    if r == l:
        return a

    m = (r + l) // 2
    mergesort(a, l, m)
    mergesort(a, m + 1, r)
    merge(a, l, m, a, m + 1, r, a, l)

def sort(a):
    return mergesort(a, 0, len(a) - 1)









import numpy as np
def is_ascending(seq):
    return not np.sum(np.diff(seq) < 0)


size = 10
cases = 300

for case in range(cases):

    a = np.random.randint(10000000, size=size)
    b = a.copy()
    sort(a)
    if (not is_ascending(a)):
        print(f"Error on: {a}")
