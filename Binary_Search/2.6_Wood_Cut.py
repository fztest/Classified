"""
Description
======================
Given n pieces of wood with length L[i] (integer array).
Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length.
What is the longest length you can get from the n pieces of wood? \Given L & k, return the maximum length of the small pieces.

Example
======================
For L=[232, 124, 456], k=7, return 114.
"""


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """

    def woodCut(self, L, k):
        if sum(L) < k:
            return 0

        maxLen = max(L)
        start, end = 1, maxLen
        while start + 1 < end:
            mid = (start + end) / 2
            pieces = sum([l / mid for l in L])
            if pieces >= k:
                start = mid
            else:
                end = mid

        if sum([l / end for l in L]) >= k:
            return end
        return start