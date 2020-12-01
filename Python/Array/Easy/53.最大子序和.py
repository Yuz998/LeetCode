#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
# https://leetcode-cn.com/problems/maximum-subarray/

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

'''

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ## 解法一：(耗时：44ms, 击败89.87%)
        # Kadane算法扫描一次整个数列的所有数值，
        # 在每一个扫描点计算以该点数值为结束点的子数列的最大和（正数和）。
        # 该子数列由两部分组成：以前一个位置为结束点的最大子数列、该位置的数值。
        # 因为该算法用到了“最佳子结构”（以每个位置为终点的最大子数列都是基于其前一位置的最大子数列计算得出, 
        # 该算法可看成动态规划的一个例子。
        # 状态转移方程：sum[i] = max{sum[i-1]+a[i],a[i]}   
        # 其中(sum[i]记录以a[i]为子序列末端的最大序子列连续和)
        
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > res[i-1]+nums[i]:
                res.append(nums[i])
            else:
                res.append(res[i-1]+nums[i])
        return max(res)


# @lc code=end

