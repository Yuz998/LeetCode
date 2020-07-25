#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
# https://leetcode-cn.com/problems/container-with-most-water/


'''

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

 



图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

 

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49

'''

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        解法一：双指针
        (耗时：24ms, 击败99.04%)
        """
        # res = 0
        # i, j = 0, len(height)-1
        # while i < j:
        #     if height[i] < height[j]:
        #         tmp_res = (j-i) * height[i]
        #         if res < tmp_res:
        #             res = tmp_res
        #         else:
        #             i += 1
        #     else:
        #         tmp_res = (j-i) * height[j]
        #         if res < tmp_res:
                    
        #             res = tmp_res
        #         else:
        #             j -= 1
        # return res


        '''
        解法一的简化版：
        (耗时:28ms, 击败96.24%)
        '''
        res = 0
        i, j = 0, len(height)-1
        while i < j:
            res_tmp = (j-i)*min(height[i], height[j])
            res = max(res, res_tmp)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res

# @lc code=end

