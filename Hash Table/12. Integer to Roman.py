class Solution(object):
    def __init__(self):
        self.number = {'1': (0, 0, 0, 1),
                 '2': (0, 0, 0, 2),
                 '3': (0, 0, 0, 3), 
                 '4': (1, 0, 1, 0),
                 '5': (0, 0, 1, 0),
                 '6': (0, 0, 1, 1),
                 '7': (0, 0, 1, 2),
                 '8': (0, 0, 1, 3),
                 '9': (1, 1, 0, 0)
                }
        self.scale = {0: ('I', 'X', 'V', 'I'),
                1: ('X', 'C', 'L', 'X'),
                2: ('C', 'M', 'D', 'C'),
                3: ('', '', '', 'M'),         
                }        
    def intToRoman(self, num):
        ans = ''
        for i, e in enumerate(str(num)[::-1]):
            if e == '0':
                continue
            elif i == '3':
                prod = self.number[e][0]*'M'
            else:
                prod = self.number[e][0]*self.scale[i][0] + \
                self.number[e][1]*self.scale[i][1] + \
                self.number[e][2]*self.scale[i][2] + \
                self.number[e][3]*self.scale[i][3]
            ans = prod + ans
        
        return ans
