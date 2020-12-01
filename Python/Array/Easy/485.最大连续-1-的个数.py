#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
# https://leetcode-cn.com/problems/max-consecutive-ones/

'''
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
'''

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            
        ## 解法一：遍历数组，遇到1统计cnt的个数，遇到0则将cnt重置为0  (使用max(),耗时：544ms)
                  # (不使用max(),耗时：412ms)
        res = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0 
            if cnt > res:
                res = cnt
            # res = max(res,cnt)
        return res

        ## 解法二：将数组转为字符串，用0分割，求最大子串长度 (耗时：488ms)
        # return max(len(substr) for substr in ''.join(str(i) for i in nums).split('0'))
# @lc code=end

