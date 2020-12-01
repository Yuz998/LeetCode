#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
# https://leetcode-cn.com/problems/majority-element/

'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

'''

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ## 解法一：用字典统计元素和元素个数   (耗时：63ms, 击败        ## 解法一：用字典存储元素和元素个数   (耗时：63ms, 击败11.54%)
        # dic = dict()
        # for i in nums:
        #     if i not in dic:
        #         dic[i] = 1
        #         # cnt = 1
        #     else:
        #         dic[i] += 1
        #     if dic[i] > len(nums)/2:
        #         return i
        
        ## 解法一的简写
        hashmap = dict()
        for i in nums:
            hashmap[i] = hashmap.get(i,0) +1

            if hashmap[i] > len(nums)/2:
                return i
# @lc code=end
