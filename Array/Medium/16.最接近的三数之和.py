#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
# https://leetcode-cn.com/problems/3sum-closest/


'''

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。


示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4


'''


# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        解法一：双指针，固定一个k遍历数组，i和j为双指针，每次判断三数之和与target之间的大小
        (耗时：68ms, 击败68.88%)
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for k in range(len(nums)):
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    return target
        return res

# @lc code=end

# %%
def threeSumClosest(nums, target):
    
    nums.sort()
    # res = nums[0] + nums[1] + nums[2]
    res = nums[0]
    for k in range(len(nums)):
        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if abs(s - target) < abs(res - target):
                res = s
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return target
    return res
threeSumClosest([-1,2,1,-4], 1)

# %%
