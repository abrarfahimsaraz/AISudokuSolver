class SudokuSolver:
    def __init__(self, input_matrix):
        self.arr = input_matrix
        self.pos = {}
        self.rem = {}
        self.graph = {}
        self.build_pos_and_rem()
        self.build_graph()

    def print_matrix(self):
        for i in range(9):
            for j in range(9):
                print(str(self.arr[i][j]), end=" ")
            print()

    def is_safe(self, x, y, key):
        for i in range(9):
            if i != y and self.arr[x][i] == key:
                return False
            if i != x and self.arr[i][y] == key:
                return False

        r_start, r_end = int(x / 3) * 3, int(x / 3) * 3 + 3
        c_start, c_end = int(y / 3) * 3, int(y / 3) * 3 + 3

        for i in range(r_start, r_end):
            for j in range(c_start, c_end):
                if i != x and j != y and self.arr[i][j] == key:
                    return False
        return True

    def fill_matrix(self, k, keys, r, rows):
        for c in self.graph[keys[k]][rows[r]]:
            if self.arr[rows[r]][c] > 0:
                continue
            self.arr[rows[r]][c] = keys[k]
            if self.is_safe(rows[r], c, keys[k]):
                if r < len(rows) - 1:
                    if self.fill_matrix(k, keys, r + 1, rows):
                        return True
                    else:
                        self.arr[rows[r]][c] = 0
                        continue
                else:
                    if k < len(keys) - 1:
                        if self.fill_matrix(k + 1, keys, 0, list(self.graph[keys[k + 1]].keys())):
                            return True
                        else:
                            self.arr[rows[r]][c] = 0
                            continue
                    return True
            self.arr[rows[r]][c] = 0
        return False

    def build_pos_and_rem(self):
        for i in range(9):
            for j in range(9):
                if self.arr[i][j] > 0:
                    if self.arr[i][j] not in self.pos:
                        self.pos[self.arr[i][j]] = []
                    self.pos[self.arr[i][j]].append([i, j])
                    if self.arr[i][j] not in self.rem:
                        self.rem[self.arr[i][j]] = 9
                    self.rem[self.arr[i][j]] -= 1

        for i in range(1, 10):
            if i not in self.pos:
                self.pos[i] = []
            if i not in self.rem:
                self.rem[i] = 9

    def build_graph(self):
        for k, v in self.pos.items():
            if k not in self.graph:
                self.graph[k] = {}

            row, col = list(range(9)), list(range(9))

            for cord in v:
                row.remove(cord[0])
                col.remove(cord[1])

            if len(row) == 0 or len(col) == 0:
                continue

            for r in row:
                for c in col:
                    if self.arr[r][c] == 0:
                        if r not in self.graph[k]:
                            self.graph[k][r] = []
                        self.graph[k][r].append(c)

    def solve_sudoku(self):
        key_s = list(self.rem.keys())
        self.fill_matrix(0, key_s, 0, list(self.graph[key_s[0]].keys()))
        


# Example usage:
input_matrix = [
    [5, 0, 1, 3, 0, 4, 0, 0, 0],
    [4, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 1, 4, 0],
    [0, 0, 0, 4, 9, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 3, 6],
    [1, 0, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 1, 7, 6, 0],
    [2, 0, 0, 0, 4, 0, 0, 0, 0],
    [6, 1, 3, 0, 0, 0, 0, 5, 9]
]

solver = SudokuSolver(input_matrix)
solver.solve_sudoku()
solver.print_matrix()
