class Solution:

    def shift(self, c, x):
        return chr(ord(c) + int(x))

    def replaceDigits(self, s: str) -> str:
        char = ''
        for i in range(len(s)):
            if i % 2 == 0:
                char += s[i]
            else:
                char += self.shift(s[i - 1], s[i])
        return char

s = Solution()

print(s.replaceDigits("a1c1e1"))