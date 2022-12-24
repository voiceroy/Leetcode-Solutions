import collections


class Solution:
    def isValidSudoku(self, board: list) -> bool:
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        blocks = collections.defaultdict(set)

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue

                if (
                    board[row][column] in rows[row]
                    or board[row][column] in columns[column]
                    or board[row][column] in blocks[(row // 3, column // 3)]
                ):
                    return False

                columns[column].add(board[row][column])
                rows[row].add(board[row][column])
                blocks[(row // 3, column // 3)].add(board[row][column])

        return True
