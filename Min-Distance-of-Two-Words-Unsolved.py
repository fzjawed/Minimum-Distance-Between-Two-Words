class Solution:
    def solve(self, text, word0, word1):
        index1 = 0
        index2 = 0
        words = list(text.split(" "))
        for i in range(0,len(words)):
            if word0 not in words or word1 not in words:
                return -1
            if words[i] == word0 and words[i+1] == word1:
                return 0
                break
            elif words[i] == word0:
                index1 = i
            elif words[i] == word1:
                index2 = i
        return (index2-index1)-1
        