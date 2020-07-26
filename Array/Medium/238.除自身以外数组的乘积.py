#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除自身以外数组的乘积
# https://leetcode-cn.com/problems/product-of-array-except-self/


'''

给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

 

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

'''


# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        解法一：分别计算出当前值左右两侧的乘积，然后左右两侧对应相乘
        (耗时：40ms, 击败63.83%)
        """
        left = 1
        right = 1
        n = len(nums)
        res_l, res_r, res = [1] * n, [1] * n, []
        for i in range(n):
            res_l[i] *= left
            left *= nums[i]
        
        for j in range(n-1, -1, -1):
            res_r[j] *= right
            right *= nums[j]
        
        for i in range(n):
            res.append(res_l[i]*res_r[i])
        return res

        '''
        解法一优化：
        (耗时：36ms, 击败78.25%)
        '''
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        r = 1
        for j in range(n-2, -1, -1):
            res[j] *= r
            r *= nums[j]
        
        return res


# @lc code=end

