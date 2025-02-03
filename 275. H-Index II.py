class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left , right = 0 , n-1
        while left <= right : 
            middle = (left + right ) // 2 
            if n - middle < citations[middle] : 
                right = middle - 1 
            else:
                left = middle + 1 
        if right < 0 : return n 
        if citations[right] > n - 1 - right :
            return citations[right]
        return n - 1 - right 