

#
# def right_bin(a, x):
#
#     l = -1
#     r = len(a)
#
#     while r - l > 1:
#         m = l + (r - l) // 2
#         if a[m] > x:
#             r = m
#         else:
#             l = m
#     return l
#
#
# def left_bin(a, x):
#
#     l = -1
#     r = len(a)
#
#     while r - l > 1:
#         m = l + (r - l) // 2
#         if a[m] >= x:
#             r = m
#         else:
#             l = m
#     return r


def left_bin(a, x):

    l = -1
    r = len(a)

    while r - l > 1:
        m = (r + l) // 2
        if a[m] >= x:
            r = m
        else:
            l = m
    return r


def right_bin(a, x):

    l = -1
    r = len(a)

    while r - l > 1:
        m = (r + l) // 2
        if a[m] > x:
            r = m
        else:
            l = m
    return l


arrays = [
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[0, 1, 4, 4, 4, 5, 6, 7, 8, 9],
[0, 1, 4, 4, 4, 5, 6, 7, 8, 9],
]

values = [
5,
4,
2
]

for arr, v in zip(arrays, values):

    print(f"Finded {v} in pos {left_bin(arr, v)} for left_bin in {arr}")
    print(f"Finded {v} in pos {right_bin(arr, v)} for right_bin in {arr}")
