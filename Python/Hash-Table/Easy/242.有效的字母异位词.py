#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
# https://leetcode-cn.com/problems/valid-anagram/

'''

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

'''


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ## 解法一：用两个字典存储元素和元素个数，判断是否相等  (耗时：60ms, 击败69.88%)
        # hashmap_s = dict()
        # hashmap_t = dict()
        # for ch in s:
        #     hashmap_s[ch] = hashmap_s.get(ch, 0) + 1

        # for ch_ in t:
        #     hashmap_t[ch_] = hashmap_t.get(ch_, 0) + 1
        
        # return hashmap_s == hashmap_t

        ## 解法二：排序 (耗时：68ms, 击败43.27%)
        # return sorted(s) == sorted(t)

        ## 解法三：使用set去重 (耗时：40ms, 击败98.72%)
        res = True
        set_tmp = set(s)
        if set_tmp == set(t):
            for i in set_tmp:
                return (s.count(i) == t.count(i)) and res
        else:
            res = False
        return res 

# @lc code=end

