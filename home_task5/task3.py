from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        foo = len(words)
        bar = []
        for i in range(0, foo):
            if x in words[i]:
                bar.append(i)
        return bar

        
cls = Solution()

print(cls.findWordsContaining(['leet', 'code'], "e"))
print(cls.findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))
print(cls.findWordsContaining(["abc","bcd","aaaa","cbc"], "z"))

# print(len(['dfghj', 'dfghj']))