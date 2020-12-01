#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。


示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

'''


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        解法一：DP思想，(耗时：52ms, 击败58.21%)
        1、记录【今天之前买入的最小值】
        2、计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
        3、比较【每天的最大获利】，取最大值即可
        转移方程（大问题与小问题的关系）
            1）定义状态：定义一个状态，例如f(i) = 到a[i]为止到最小值
            2）设计转移方程：根据如上状态方程定义，则有 f(i+1) = min(f(i), a[i+1])
        '''
        if len(prices) == 0:
            return 0
        min_ = prices[0]
        res = 0
        for i in range(1,len(prices)):
            min_ = min(min_, prices[i])
            res = max(prices[i]-min_, res)
        return res

# @lc code=end

