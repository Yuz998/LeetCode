#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
# https://leetcode-cn.com/problems/plus-one/submissions/


'''

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。


'''

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        解法一：遍历数组，遇到9，该位置值0，遇到非9 则加一，
        如果第0位为0，则插入1.
        (耗时：16ms, 击败89.56)
        """
        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] != 9:
        #         digits[i] += 1
        #         return digits
        #     else:
        #         digits[i] = 0
        #         if digits[0] == 0:
        #             digits.insert(0, 1)
        #             return digits

        '''
        解法二：列表转整数然后加一，在转回列表
        list->str->int->str->list
        (耗时：24ms, 击败45.45%)
        '''
        str_num = ''.join(str(i) for i in digits)
        int_num = str(int(str_num)+1)
        return [int(i) for i in str(int_num)]



# @lc code=end

