class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # return self.knapsackRecursive(word1, word2, len(word1) - 1, len(word2) - 1)

        # dp = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
        # return self.knapsackTopDown(word1, word2, len(word1) - 1, len(word2) - 1, dp)

        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        return self.bottomUp(word1, word2, dp)

    def knapsackRecursive(self, word1, word2, index1, index2):
        if index1 < 0: return index2 + 1
        if index2 < 0: return index1 + 1

        if word1[index1] == word2[index2]: return self.knapsackRecursive(word1, word2, index1 - 1, index2 - 1)
        else:
            insert = self.knapsackRecursive(word1, word2, index1, index2 - 1) + 1
            delete = self.knapsackRecursive(word1, word2, index1 - 1, index2) + 1
            replace = self.knapsackRecursive(word1, word2, index1 - 1, index2 - 1) + 1
            return min(insert, delete, replace)
    
    def knapsackTopDown(self, word1, word2, index1, index2, dp):
        if index1 < 0: return index2 + 1
        if index2 < 0: return index1 + 1

        if word1[index1] == word2[index2]:
            if dp[index1][index2] == 0: dp[index1][index2] = self.knapsackTopDown(word1, word2, index1 - 1, index2 - 1, dp)
            return dp[index1][index2]
        else:
            if dp[index1][index2] == 0:
                dp[index1][index2] = min(
                    self.knapsackTopDown(word1, word2, index1, index2 - 1, dp) + 1,
                    self.knapsackTopDown(word1, word2, index1 - 1, index2, dp) + 1,
                    self.knapsackTopDown(word1, word2, index1 - 1, index2 - 1, dp) + 1
                )
            return dp[index1][index2]

    def bottomUp(self, word1, word2, dp):
        if word1 == word2: return 0
        if len(word1) == 0: return len(word2)
        if len(word2) == 0: return len(word1)

        dp[0][0] = 0
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        
        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]: dp[i][j] = dp[i - 1][j - 1]
                else: dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[len(word1)][len(word2)] 
