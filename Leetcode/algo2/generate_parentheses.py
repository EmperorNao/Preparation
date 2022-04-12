class Solution:

    def generate(self, left, right, cur_seq, all_seq):

        if left == 0 and right == 0:
            all_seq.append("".join(cur_seq))
            return

        if left != 0:
            cur_seq.append('(')
            self.generate(left - 1, right, cur_seq, all_seq)
            cur_seq.pop()

        if left < right:
            cur_seq.append(')')
            self.generate(left, right - 1, cur_seq, all_seq)
            cur_seq.pop()

    def generateParenthesis(self, n: int) -> List[str]:

        sol = []
        cur = []
        self.generate(n, n, cur, sol)

        return sol
