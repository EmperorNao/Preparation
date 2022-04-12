

def generate(left, right, cur_seq, all_seq):

    if left == 0 and right == 0:
        all_seq.append("".join(cur_seq))
        return

    if left != 0:
        cur_seq.append('(')
        generate(left - 1, right, cur_seq, all_seq)
        cur_seq.pop()

    if left < right:
        cur_seq.append(')')
        generate(left, right - 1, cur_seq, all_seq)
        cur_seq.pop()



all_seq = []
cur_seq = []
n = int(input())

generate(n, n, cur_seq, all_seq)
print("\n".join(all_seq))
