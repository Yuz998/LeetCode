#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
# https://leetcode-cn.com/problems/valid-palindrome/

'''

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

'''

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        解法一: 使用string.isalnum()函数  
        如果 string 至少有一个字符并且所有字符都是字母或数字
        则返回True,否则返回False
        (耗时: 40ms, 击败78.95%)
        """
        s_t = ''.join(i.lower() for i in s if i.isalnum())
        return s_t[::-1] == s_t
        
# @lc code=end

