class Solution:
    def solve(self, text, word0, word1):
        words = list(text.split(" "))
        dist = len(words) + 1
        if word0 in words and word1 in words:
            for i in range(0,len(words)):
                if words[i] == word0 or words[i] == word1:
                    prev = i
                    break
            while i < len(words):
                if words[i] == word0 or words[i] == word1:
                    if words[prev] != words[i] and (i-prev) < dist:
                        dist = (i-prev) - 1
                        prev = i
                    else:
                        prev = i
                i += 1
        else: 
            return -1
        return dist