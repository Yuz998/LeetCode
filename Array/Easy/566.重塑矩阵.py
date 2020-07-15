#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
# https://leetcode-cn.com/problems/reshape-the-matrix/


# 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

# 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

# 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

# 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

# 示例 1:

# 输入: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# 输出: 
# [[1,2,3,4]]
# 解释:
# 行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
# 示例 2:

# 输入: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# 输出: 
# [[1,2],
#  [3,4]]
# 解释:
# 没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
# 注意：

# 1.给定矩阵的宽和高范围在 [1, 100]。
# 2.给定的 r 和 c 都是正数。



# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        ## 解法一：首先将二维变成一维数组，然后使用切片 (耗时：108ms)
        # num = []
        # res = []
        # if len(nums) * len(nums[0]) != r*c:
        #     return nums
        # else:
        #     for i in range(len(nums)):
        #         for j in range(len(nums[0])):
        #             num.append(nums[i][j])
                    
        #     for i in range(0,len(num),c):
        #         res.append(num[i:i+c])

        #     return res

        ## 间接写法：(耗时：112ms)
        if len(nums) * len(nums[0]) != r*c:
            return nums
        res = [i for j in nums for i in j]
        return [res[i:i+c] for i in range(0,len(res),c)]
# @lc code=end
