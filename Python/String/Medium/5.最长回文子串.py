#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
# https://leetcode-cn.com/problems/longest-palindromic-substring/

'''

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"


'''

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        解法一：两边穷举，无法通过
        """
        # cnt = 0
        # res = ''
        # for right in range(len(s), -1, -1):
        #     # for left in range(len(s)-right+1):
        #     for left in range(right):
        #         sub_str = s[left: right]
        #         # print(sub_str)
        #         # sub_str = s[left: right + left]
        #         if sub_str == sub_str[::-1] and cnt < len(sub_str):
        #             res = sub_str
        #             cnt = len(sub_str)
        # return res

        '''
        解法二：长度逐渐缩短
        (耗时: 4956ms, 击败12.8%)
        '''
        # for right in range(len(s), -1, -1):
        #     for left in range(len(s)-right+1):
        #         sub_str = s[left: right + left]
        #         if sub_str == sub_str[::-1]:
        #             return sub_str
        
        '''
        解法三：中心扩散法，枚举中心位置，每一次向两边扩散监测是否为回文串
        (耗时：596ms, 击败86.09%)
        '''
        n = len(s)
        ## 判断[l:r]字符串是否为回文串
        def getLen(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        ## 起始位置和长度为0
        start = lenght = 0
        for i in range(n):
            ## 取奇数回文串和偶数回文串的最大值
            cur = max(getLen(i, i), getLen(i, i + 1))
            if cur <= lenght:
                continue
            lenght = cur
            start = i - (cur - 1) // 2
        return s[start: start + lenght]
# @lc code=end

