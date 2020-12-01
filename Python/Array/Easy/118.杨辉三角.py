#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
# https://leetcode-cn.com/problems/pascals-triangle/


'''

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。


在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        解法一：迭代方式
        (耗时: 24ms, 击败30.12%)
        """
        # res = []
        # for i in range(numRows):
        #     row = [None for _ in range(i+1)]
        #     row[0], row[-1] = 1, 1

        #     for j in range(1, len(row)-1):
        #         row[j] = res[i-1][j-1] + res[i-1][j]
            
        #     res.append(row)
        # return res

        '''
        解法二：错位相加, 使用zip函数对最后一行的前面和后面加0之后相加。
        (耗时: 16ms, 击败80.17%)
        '''
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRows = [i+j for i,j in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRows)
        return res

# @lc code=end

