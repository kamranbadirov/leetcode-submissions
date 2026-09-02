class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == '.':
                    continue
                row = i
                col = j
                box = (i // 3 ) * 3 + (j // 3)
                if val in rows[row] or val in cols[col] or val in boxes[box]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                boxes[box].add(val)
        return True

        