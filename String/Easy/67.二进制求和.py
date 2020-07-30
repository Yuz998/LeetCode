#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
# https://leetcode-cn.com/problems/add-binary/

'''

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

'''

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        解法一：使用int()函数强制转换相加，再将其转换为二进制
        (耗时：20ms, 击败84.48%)
        """
        # return bin(int(a, 2)+int(b, 2))[2:]

        '''
        解法二：大数相加的思想，设置一个进位符
        (耗时：76ms, 击败8.54%)
        '''
        # if not a or not b: return a or b
        res = ''
        # carry: 进位 
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            n1 = int(a[i]) if i >= 0 else 0
            n2 = int(b[j]) if j >= 0 else 0
            cur = (n1 + n2 + carry) % 2
            carry = (n1 + n2 + carry) // 2
            # carry, cur = divmod(n1 + n2 + carry, 2) divmod()函数返回商和余数
            print(n1, n2)
            print(cur, carry)
            res = str(cur) + res
            i, j = i - 1, j - 1
        return '1' + res if carry else res
# @lc code=end
