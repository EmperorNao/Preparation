def d_from_num(nums):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 0
        d[n] += 1
    return d


class Solution:

    def find_combinations(self, keys, nums, pos, target, cur_seq, cur_sum):

        if cur_sum == target:
            self.sol.append(cur_seq[:])
            return

        if pos >= len(keys):
            return

        self.find_combinations(keys, nums, pos + 1, target, cur_seq, cur_sum)

        cnt = 0
        while nums[keys[pos]] > 0 and cur_sum + keys[pos] <= target:

            cur_seq.append(keys[pos])
            nums[keys[pos]] -= 1
            cur_sum += keys[pos]
            self.find_combinations(keys, nums, pos + 1, target, cur_seq, cur_sum)
            cnt += 1

        nums[keys[pos]] += cnt
        for i in range(cnt):
            cur_seq.pop()
            cur_sum -= keys[pos]


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.sol = []
        cur_seq = []
        d = d_from_num(candidates)
        self.find_combinations(list(reversed(sorted(list(d.keys())))), d, 0, target, cur_seq, 0)
        return self.sol
