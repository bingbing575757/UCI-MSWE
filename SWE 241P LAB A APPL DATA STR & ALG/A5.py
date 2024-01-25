#Task-1:

from collections import Counter

def is_permutation(s1, s2):
    count_s1 = Counter(s1)
    count_window = Counter(s2[:len(s1)])

    if count_window == count_s1:
        return True

    for i in range(len(s1), len(s2)):
        count_window[s2[i - len(s1)]] -= 1
        if count_window[s2[i - len(s1)]] == 0:
            del count_window[s2[i - len(s1)]]
        count_window[s2[i]] += 1

        if count_window == count_s1:
            return True

    return False


# Sample Test Cases
print(is_permutation("abooo", "eidbaooo"))  # True
print(is_permutation("ab", "eidboaoo"))  # False



# Task-2

class Solution:
    def solveNQueens(self, n: int):
        result = []
        chessboard = [[0 for _ in range(n)] for _ in range(n)]
        self.backtracking(n, 0, chessboard, result)
        return result

    def backtracking(self, n: int, row: int, chessboard, result):
        if row == n:
            result.append([row[:] for row in chessboard])
            return

        for col in range(n):
            if self.isValid(row, col, chessboard):
                chessboard[row][col] = 1  # Put a queen
                self.backtracking(n, row + 1, chessboard, result)
                chessboard[row][col] = 0 # Delete a queen and continue backtracking

    def isValid(self, row: int, col: int, chessboard):
        # Check the column
        for i in range(row):
            if chessboard[i][col] == 1:
                return False  # Already a queen in this column, not valid

        # Check top left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 1:
                return False  # Already a queen in the top left diagonal, not valid
            i -= 1
            j -= 1

        # Check top right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 1:
                return False  # Already a queen in the top right diagonal, not valid
            i -= 1
            j += 1

        return True  # Valid


# Test: n = 8
solution = Solution()
result = solution.solveNQueens(8)
print(result)
print(len(result))
reverse_result = []
for Q in result:
    tmp = []
    transposed_matrix = list(zip(*Q))
    for row in transposed_matrix:
        tmp.append(list(row))
    reverse_result.append(tmp)
print(reverse_result)
index = []
for Q in reverse_result:
    column_indices = [index+1 for row in Q for index, element in enumerate(row) if element == 1]
    index.append(column_indices)
print(index)


input = [1, 2, 3, 4, 5, 6, 7, 8]
sum = []
for Q in index:
    tmp = 0
    for i in range(len(input)):
        if abs(Q[i]-input[i]) != 0:
            tmp += 1
    sum.append(tmp)
print(min(sum))





