
class Solution:

    ## numbers is reversed sorted array ## or maybe not
    def generate_seq(self, numbers, pos, sum, target, cur_seq, sol):

        if sum == target:
            sol.append(cur_seq[:])

        if pos >= len(numbers):
            return

        self.generate_seq(numbers, pos + 1, sum, target, cur_seq, sol)
        cnt = 0
        while sum + numbers[pos] <= target:

            cur_seq.append(numbers[pos])
            sum += numbers[pos]
            self.generate_seq(numbers, pos + 1, sum, target, cur_seq, sol)
            cnt += 1

        for i in range(cnt):
            cur_seq.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur_seq = []
        sol = []
        self.generate_seq(candidates, 0, 0, target, cur_seq, sol)
        return sol
