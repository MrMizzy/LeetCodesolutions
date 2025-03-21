class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number = 0
        for i in range(len(s)-1):
            if mapping[s[i]] >= mapping[s[i+1]]:
                number += mapping[s[i]]
            else:
                number -= mapping[s[i]]
        number += mapping[s[-1]]
        return number