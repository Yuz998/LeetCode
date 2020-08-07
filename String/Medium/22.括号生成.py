#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/

'''

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]


'''

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        解法一：回溯法 dfs
        (耗时：20ms，击败76.73%)
        """
    #     if n == 0:
    #         return []
    #     res = []
    #     self.dfs(n, n, '', res)
    #     return res
    
    # def dfs(self, l, r, item, res):
    #     '''
    #     l: 左括号剩余数量
    #     r: 右括号剩余数量
    #     item: 已有的符号
    #     res: 结果
    #     '''
    #     ## 去除不合法的符号
    #     if r < l :
    #         return

    #     if l == 0 and r ==0:
    #         res.append(item)
    #     if l > 0:
    #         self.dfs(l - 1, r, item + '(', res)
    #     if r > 0:
    #         self.dfs(l, r - 1, item + ')', res)

    
        ''''
        解法二：构造递归公式f(n) = f(n - 1)，在不同的位置上插入"()"， 然后去重
        (耗时：16ms, 击败91.8%)
        '''
        if n == 0:
            return []

        pre = ['()', ]
        for i in range(n - 1):
            now = set()
            for ch in pre:
                n = len(ch)
                for index in range(n):
                    now.add(ch[: index] + "()" + ch[index:])
            pre = now
            
        return list(pre)
# @lc code=end

