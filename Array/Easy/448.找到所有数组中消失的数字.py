#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/

'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

'''

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        '''
        解法一：使用集合的差集  (耗时：408ms, 击败94.82%)
        '''
        # return list(set([i for i in range(1,len(nums)+1)])-set(nums))

        '''
        解法二：用字典统计元素个数, 遍历list, 不在hashmap里面则为消失的数字 (耗时：428ms, 击败83.83%)
        '''
        hashmap = dict()
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        res = []
        for i in range(1, len(nums)+1):
            if i not in hashmap:
                res.append(i)
        return res

# @lc code=end

