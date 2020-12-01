#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
# https://leetcode-cn.com/problems/maximum-product-subarray/

'''

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 
示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

'''

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        解法一：DP思想：使用dp数组来表示前i个元素的最大乘积
        (耗时: 28ms, 击败66.77%%)
        """
        res = nums[0]
        n = len(nums)
        mul_max, mul_min = [0] * n, [0] * n
        mul_max[0], mul_min[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            ## 如果当前值大于等于0，则最大值为当前值乘以前i的最大值与当前值较大的那个
            if nums[i] >= 0:
                mul_max[i] = max(mul_max[i - 1] * nums[i], nums[i])
                mul_min[i] = min(mul_min[i - 1] * nums[i], nums[i])
            ## 如果当前值小于0，则最大值为当前值乘以前i的最小值与当前值较大的那个
            else:
                mul_max[i] = max(mul_min[i - 1] * nums[i], nums[i])
                mul_min[i] = min(mul_max[i - 1] * nums[i], nums[i])
            
            res = max(res, mul_max[i])
        return res

        '''
        解法二：统计左右两侧连续乘机之和，遇到0则重置
        (耗时：20ms, 击败94.47%)
        '''
        # rev_num = nums[::-1]
        # for i in range(1, len(nums)):
        #     nums[i] *= nums[i - 1] or 1
        #     rev_num[i] *= rev_num[i - 1] or 1
        # print(nums, rev_num)
        # return max(nums + rev_num)
        
# @lc code=end

