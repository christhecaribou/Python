# CHRIS FELLI, 2019
# Given an int array, calculate how water
# could be stored topographically
from typing import List


class Solution:
    def _init(self, bars=[]):
        self.bars = bars

    def trap(self, bars: List[int]) -> int:
        if not bars or len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume


# Driver
test = Solution()
print(test.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
