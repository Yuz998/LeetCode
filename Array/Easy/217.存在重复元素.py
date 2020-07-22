#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
# https://leetcode-cn.com/problems/contains-duplicate/

'''

给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

'''


# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        解法一: 转化为集合，再转化为列表，比较两个列表的长度
        (耗时：28ms, 击败67.92%)
        """
        # if len(nums) - len(list(set(nums))) >=1:
        #     return True
        # else:
        #     return False

        return len(nums) != len(list(set(nums)))

# @lc code=end
