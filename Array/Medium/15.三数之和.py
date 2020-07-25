#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
# https://leetcode-cn.com/problems/3sum/

'''

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        解法一：双指针：固定一个k(遍历整个数组)，i和j为双指针，同时判断相邻两个数是否相同
        (耗时528ms:, 击败65.24%)
        """
        nums.sort()
        k, res =  0, []
        for k in range(len(nums) - 2):
            ## 如果第一个数大于0，则没有满足条件的三元组
            if nums[k] > 0: break  
            ## 如果相邻两个数相同，则跳过
            if k > 0 and nums[k] == nums[k - 1]: continue
            ## 双指针开始
            i, j = k + 1, len(nums) - 1
            
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                     ## 如果相邻两个数相同，则继续
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                     ## 如果相邻两个数相同，则继续
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
         
        return res

# @lc code=end

