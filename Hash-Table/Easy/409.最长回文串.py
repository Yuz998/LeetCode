#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
# https://leetcode-cn.com/problems/longest-palindrome/

'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

'''


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        ## 解法一：遍历set，如果ch为奇数p加一，最后减去奇数个数在加一
        ## (耗时：32ms, 击败98.61%)
        p = 0
        for ch in set(s):
            if s.count(ch) % 2 != 0:
                p += 1
        if p == 0:
            return len(s)
        return len(s) - p + 1

# @lc code=end

