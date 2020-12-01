#
# @lc app=leetcode.cn id=680 lang=python
#
# [680] 验证回文字符串 Ⅱ
# https://leetcode-cn.com/problems/valid-palindrome-ii/

'''

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000


'''

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        解法一：暴力遍历 无法通过
        """
        # if s == s[::-1]:
        #     return True
        # else:
        #     for i in range(len(s)):
        #         tmp = s[0:i] + s[i + 1:]
        #         if tmp == tmp[::-1]:
        #             return True
                    
        '''
        解法二：双指针，降低时间复杂度
        (耗时: 68ms, 击败86.26%)
        '''
        ## 定义判断是否为回文数的函数
        def isPalindrome(x):
            return x == x[::-1]
        i, j = 0, len(s) - 1
        while i< j:
            if s[i] != s[j]:
                return isPalindrome(s[i + 1: j + 1]) or isPalindrome(s[i:j])
            else:
                i += 1
                j -= 1
        return True
        
# @lc code=end
