#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ## 解法一：字典形成一一映射 
        ## (耗时：56ms, 击败47.35%)
        hashmap = dict()
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False
                hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] != t[i]:
                    return False
        return True
# @lc code=end

