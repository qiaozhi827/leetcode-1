class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == 0:
            return '0'
        stack = [num[0]]

        for i in range(1,len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])

        if k > 0:
            stack = stack[:-k]

        while stack and stack[0] == '0':
            stack.pop(0)
        if len(stack) == 0:
            return '0'
        else:
            return ''.join(stack)

