#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
# https://leetcode-cn.com/problems/merge-intervals/

'''

给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


'''

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        解法一： 分两种情况讨论，1) 相交; 2) 不相交
        (耗时：24ms, 击败95.84%)
        """
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            ## (x1, x2) (y1, y2)  x2 < y1  不相交
            if res[-1][-1] < intervals[i][0]:
                res.append(intervals[i])
            ## 相交  [x1, max(x2, y2)]
            else:
                res[-1][-1] = max(res[-1][-1], max(res[-1][-1], intervals[i][1]))
        return res


# @lc code=end


