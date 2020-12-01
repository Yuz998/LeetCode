#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

'''
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
'''

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        ## 解法一：先排序，在对比，得到不同的最大最小下标，相减即可。(耗时：232ms,击败99.33%)
        low = 0
        high = len(nums) - 1
        nums_sort = sorted(nums)
        while low <= high and nums[low] == nums_sort[low]:
            low += 1
        while low <= high and nums[high] == nums_sort[high]:
            high -= 1
        return high - low + 1

        ## 解法一简化版：(耗时：264ms, 击败63.57%)
        diff = [i for i, (a,b) in enumerate(zip(nums,sorted(nums))) if a!=b]
        return len(diff) and max(diff) - min(diff) + 1
# @lc code=end

