

n = int(input())


cur_seq = 0
max_seq = 0

for i in range(n):

    b = input()
    if b == '0':
        if cur_seq > max_seq:
            max_seq = cur_seq
        cur_seq = 0

    else:
        cur_seq += 1

if cur_seq > max_seq:
    max_seq = cur_seq


print(max_seq)
