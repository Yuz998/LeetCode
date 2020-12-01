#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
# https://leetcode-cn.com/problems/palindrome-number/

'''

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

'''

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        解法一：将整型转为字符串，判断反转后的与原字符串是否相同
        (耗时：64ms, 击败99.06%)
        '''
        # if str(x)[::-1] == str(x):
        #     return True
        # else:
        #     return False

        '''
        解法二：非字符串法
        (耗时：104ms, 击败24.75%)
        '''
        if x < 0 or (x!=0 and x%10 ==0):
            return False
        elif x == 0:
            return True
        else:
            rev = 0
            while x > rev:
                rem = x % 10
                rev = rev * 10 + rem
                x //= 10
            if rev == x or rev // 10 == x:
                return True
            else:
                return False

# @lc code=end

