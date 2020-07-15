#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/


# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]

# 示例 2:
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]

# 说明：
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ## 解法一： 暴力遍历两个数组 (耗时：96ms) 
        # res = []
        # for i in nums1:
        #     if i in nums2:
        #         res.append(i)
        #         nums2.remove(i)
        # return res 

        ## 解法二： 字典模拟哈希表 (耗时：76ms) 
        # dict_num = {}
        # res = []
        # for i in nums1:
        #     if i in dict_num:
        #         dict_num[i] += 1
        #     else:
        #         dict_num[i] = 1
        # for i in nums2:
        #     if i in dict_num and dict_num[i] > 0:
        #         res.append(i)
        #         dict_num[i] -= 1
        # return res

        ## 解法三：先排序，再使用双指针(i,j相当于两个指针)  (耗时最短：68ms) 
        nums1.sort()
        nums2.sort()
        res = []
        i=j=0  ## 双指针
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res 
# @lc code=end



