class Solution(object):
    def numRabbits(self, answers):
        ans = 0
        dct = Counter(answers)
        for n, rabbits in dct.items():
            if not n:
                ans += rabbits
            else:
                ans += bool(rabbits%(n + 1))*(n + 1) + (n + 1)*(rabbits//(n + 1))
        return ans
