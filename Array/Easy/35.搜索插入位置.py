#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
# https://leetcode-cn.com/problems/search-insert-position/


# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。

# 示例 1:

# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:

# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:

# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:

# 输入: [1,3,5,6], 0
# 输出: 0

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## 解法一：暴力穷举  (耗时：48ms)
        # if nums[len(nums)-1] < target:
        #     return len(nums)
        # elif nums[len(nums)-1] == target:
        #     return len(nums)-1
        # if len(nums) == 1 and nums[0] > target:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i] == target:
        #         return i
        #     elif nums[i] > target:
        #         return 0
        #     else:
        #         if nums[i+1] > target:
        #             return i+1
        #         elif nums[i+1] < target:
        #             continue
        
        ## 解法二：求小于target的list长度  (耗时：44ms)
        # return len([i for i in nums if i < target])

        ## 解法三：二分查找  (耗时：40ms)
        left = 0
        right = len(nums)
        while left < right:
            mid =left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left

# @lc code=end

# %%
def searchInsert(nums, target):
    if nums[len(nums)-1] < target:
        return len(nums)
    elif nums[len(nums)-1] == target:
        return len(nums)-1
    if len(nums) == 1 and nums[0] > target:
        return 0
    for i in range(len(nums)-1):
        # print(i,nums[i])
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return 0
        else:
            if nums[i+1] > target:
                return i+1
            elif nums[i+1] < target:
                continue

searchInsert([1],0)

# %%
