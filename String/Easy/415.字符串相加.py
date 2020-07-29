#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
# https://leetcode-cn.com/problems/add-strings/

'''

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

'''


# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        解法一：使用int强制转换
        (耗时：20ms, 击败97.01%)
        """
        # return str(int(num1)+int(num2))
        return str(eval(num1 + '+' + num2))
        
        '''
        解法二：使用大数相加的思想，定义一个进位遍历carry
        (耗时：28ms, 击败92.03%)
        '''
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[i]) if j >= 0 else 0
            tmp = a + b + carry # 对应位数相加，然后再加上进位
            carry = tmp // 10 
            res = str(tmp % 10) + res
            i -= 1
            j -= 1
        return "1" + res if carry else res

# @lc code=end
