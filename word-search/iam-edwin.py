from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for mIndex, row in enumerate(board):
            for nIndex, letter in enumerate(row):
                if letter == word[0]:
                    if self.existWithStart(board, word, mIndex, nIndex):
                        return True

        return False

    def existWithStart(self, board, word, mIndex, nIndex) -> bool:
        used = [(-1, -1)]
        return self.moveRecursive(board, word[1:], mIndex, nIndex, used)

    def moveRecursive(self, board, remainWord, mIndex, nIndex, used: List[str]) -> bool:
        if len(remainWord) == 0:
            return True

        # down
        if self.canMove(board, remainWord[0], mIndex + 1, nIndex, used):
            used.append((mIndex, nIndex))
            if self.moveRecursive(board, remainWord[1:], mIndex + 1, nIndex, used):
                return True

        # up
        if self.canMove(board, remainWord[0], mIndex - 1, nIndex, used):
            used.append((mIndex, nIndex))
            if self.moveRecursive(board, remainWord[1:], mIndex - 1, nIndex, used):
                return True

        # right
        if self.canMove(board, remainWord[0], mIndex, nIndex + 1, used):
            used.append((mIndex, nIndex))
            if self.moveRecursive(board, remainWord[1:], mIndex, nIndex + 1, used):
                return True

        # left
        if self.canMove(board, remainWord[0], mIndex, nIndex - 1, used):
            used.append((mIndex, nIndex))
            if self.moveRecursive(board, remainWord[1:], mIndex, nIndex - 1, used):
                return True

        used.pop()
        return False

    def canMove(self, board, letter, mIndex, nIndex, used) -> bool:
        m = len(board)
        n = len(board[0])

        return (
            mIndex >= 0
            and mIndex < m
            and nIndex >= 0
            and nIndex < n
            and (mIndex, nIndex) not in used
            and board[mIndex][nIndex] == letter
        )
