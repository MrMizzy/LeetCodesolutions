class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        new_citations = sorted(citations,reverse=True)
        papers = len(new_citations)
        if papers == 1:
            if new_citations[0] == 0:
                return 0
            else:
                return 1
        for i in range(papers):
            if new_citations[i]<i+1:
                return i
        return papers