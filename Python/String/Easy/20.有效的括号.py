#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
# https://leetcode-cn.com/problems/valid-parentheses/

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

'''


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
       
        # 解法一: 用list模拟栈 (耗时：28ms, 击败99.53%)
        # stack = ['?']
        # hashmap = {'[':']', '(': ')', '{': '}', '?': '?'}
        # for ch in s:
        #     if ch in hashmap:
        #         stack.append(ch)  ## 入栈
        #     elif hashmap[stack.pop()] != ch: ## 出栈
        #         return False
        # return len(stack) == 1

        ## 解法二：用字符串replace()方法 (耗时：52ms, 击败22.08%)
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '')
            s = s.replace('()', '')
            s = s.replace('{}', '')
        return s == ''
# @lc code=end

