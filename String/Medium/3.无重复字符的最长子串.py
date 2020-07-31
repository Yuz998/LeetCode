#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

'''

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        解法一：哈希法
        (耗时：40ms, 击败98.15%)
        """
        ## k记录起始下标，hashmap存放当前字符和最新下标
        k, res, hashmap = -1, 0, dict()
        for i, v in enumerate(s):
            ## 如果当前字符在哈希表里，并且当前长度的起始下标小于上次出现的下标
            ## 则移动当前长度起始下标，更新上次出现的下标
            if v in hashmap and k < hashmap[v]:
                k = hashmap[v]
                hashmap[v] = i
            else:
                hashmap[v] = i
                res = max(res, i - k)
        return res


# @lc code=end

