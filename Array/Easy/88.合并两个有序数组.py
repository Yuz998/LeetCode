#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
# https://leetcode-cn.com/problems/merge-sorted-array/

'''

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

'''


# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        解法一：使用切片相加后排序
        (耗时：16ms, 击败90.07%)
        """
        # nums1[:] = sorted(nums1[:m] + nums2[:n])

        '''
        解法二：双指针
        (耗时：24ms, 击败50.1%)
        '''
        nums1_copy = nums1[:m]
        nums1[:] = []
        i = j = 0
        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        
        if i < m:
            nums1[i+j:] = nums1_copy[i:] 
        if j < n:
            nums1[i+j:] = nums2[j:]

# @lc code=end
