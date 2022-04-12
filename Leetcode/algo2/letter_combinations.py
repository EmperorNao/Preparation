

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = {
        '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs',
        '8':'tuv', '9':'wxyz'
        }


        sol = [[]]
        for ch in digits:

            new_sol = []
            for s in sol:
                for dig in self.digits[ch]:
                    new_sol.append(s + [dig])

            sol = new_sol

        return ["".join(s) for s in sol]
