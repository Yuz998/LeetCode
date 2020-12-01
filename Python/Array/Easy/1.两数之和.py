#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和  Simple
# https://leetcode-cn.com/problems/two-sum/


# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 解法二：哈希 (耗时：60ms)
        hashmap = dict()
        for v,k in enumerate(nums):
            hashmap[k] = v
        for i,q in enumerate(nums):
            tar = target - q
            j = hashmap.get(tar)
            if j != i and j is not None:
                return [i,j]

# @lc code=end
