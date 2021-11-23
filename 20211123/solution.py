# 给出一个字符串 s（仅含有小写英文字母和括号）。
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 注意，您的结果中 不应 包含任何括号。

# 示例 1：
#
# 输入：s = "(abcd)"
# 输出："dcba"

# 示例 2：
#
# 输入：s = "(u(love)i)"
# 输出："iloveu"
# 解释：先反转子字符串 "love" ，然后反转整个字符串。

# 示例 3：
#
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
# 解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。

# 示例 4：
#
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"

class Solution:
    def reverseParentheses(self, s: str) -> str:
        res_left = ''
        res_right = ''
        left_p = 0
        right_p = len(s) - 1
        side = 0
        flag = 0
        while left_p <= right_p:
            if side == 0:
                if s[left_p] == '(':
                    side = 1
                else:
                    res_right = s[left_p] + res_right
                left_p += 1
            else:
                if s[right_p] == ')':
                    side = 0
                    flag += 1
                    res_left, res_right = res_right[::-1], res_left[::-1]
                else:
                    res_left += s[right_p]
                right_p -= 1
        if flag % 2:
            return res_left + res_right
        else:
            return (res_left + res_right)[::-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseParentheses("(abcd)"))
    print(solution.reverseParentheses("(u(love)i)"))
    print(solution.reverseParentheses("(ed(et(oc))el)"))
    print(solution.reverseParentheses("apmnolkjihgfedcbq"))
    print(solution.reverseParentheses("ta()usw((((a))))"))
