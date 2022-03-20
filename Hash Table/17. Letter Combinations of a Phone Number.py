class Solution(object):
    def __init__(self):
        self.leters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
   
        ans = [self.leters[i] for i in digits]        
        ans = itertools.product(*ans)
        
        return [''.join(a) for a in ans]
