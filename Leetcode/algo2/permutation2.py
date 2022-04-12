

def d_from_num(nums):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 0
        d[n] += 1
    return d

def sub_d(d, val):
    d[val] -= 1
    if d[val] == 0:
        d.pop(val)

def add_d(d, val):
    if val not in d:
        d[val] = 0
    d[val] += 1


class Solution:

    def generate_perm(self, d, cur, sol):
        if not d:
            sol.append(cur[:])
            return

        keys = list(d.keys())
        for v in keys:

            cur.append(v)
            sub_d(d, v)
            self.generate_perm(d, cur, sol)
            add_d(d, v)
            cur.pop()


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        d = d_from_num(nums)
        sol = []
        cur = []
        self.generate_perm(d, cur, sol)
        return sol
