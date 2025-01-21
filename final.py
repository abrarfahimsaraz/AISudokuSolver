from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic, QtGui

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("sudokuUI.ui", self)
        self.show()
        self.matrix = [[0] * 9 for _ in range(9)]

        self.pushButton.clicked.connect(self.solve)

    
    def solve(self):
        self.input()

        solver = SudokuSolver(self.matrix)
        self.matrix = solver.solve_sudoku()

        self.output()

    def input(self):
        self.matrix[0][0] = int(self.cB00.currentText())
        self.matrix[0][1] = int(self.cB01.currentText())
        self.matrix[0][2] = int(self.cB02.currentText())
        self.matrix[0][3] = int(self.cB03.currentText())
        self.matrix[0][4] = int(self.cB04.currentText())
        self.matrix[0][5] = int(self.cB05.currentText())
        self.matrix[0][6] = int(self.cB06.currentText())
        self.matrix[0][7] = int(self.cB07.currentText())
        self.matrix[0][8] = int(self.cB08.currentText())

        self.matrix[1][0] = int(self.cB10.currentText())
        self.matrix[1][1] = int(self.cB11.currentText())
        self.matrix[1][2] = int(self.cB12.currentText())
        self.matrix[1][3] = int(self.cB13.currentText())
        self.matrix[1][4] = int(self.cB14.currentText())
        self.matrix[1][5] = int(self.cB15.currentText())
        self.matrix[1][6] = int(self.cB16.currentText())
        self.matrix[1][7] = int(self.cB17.currentText())
        self.matrix[1][8] = int(self.cB18.currentText())

        self.matrix[2][0] = int(self.cB20.currentText())
        self.matrix[2][1] = int(self.cB21.currentText())
        self.matrix[2][2] = int(self.cB22.currentText())
        self.matrix[2][3] = int(self.cB23.currentText())
        self.matrix[2][4] = int(self.cB24.currentText())
        self.matrix[2][5] = int(self.cB25.currentText())
        self.matrix[2][6] = int(self.cB26.currentText())
        self.matrix[2][7] = int(self.cB27.currentText())
        self.matrix[2][8] = int(self.cB28.currentText())

        self.matrix[3][0] = int(self.cB30.currentText())
        self.matrix[3][1] = int(self.cB31.currentText())
        self.matrix[3][2] = int(self.cB32.currentText())
        self.matrix[3][3] = int(self.cB33.currentText())
        self.matrix[3][4] = int(self.cB34.currentText())
        self.matrix[3][5] = int(self.cB35.currentText())
        self.matrix[3][6] = int(self.cB36.currentText())
        self.matrix[3][7] = int(self.cB37.currentText())
        self.matrix[3][8] = int(self.cB38.currentText())

        self.matrix[4][0] = int(self.cB40.currentText())
        self.matrix[4][1] = int(self.cB41.currentText())
        self.matrix[4][2] = int(self.cB42.currentText())
        self.matrix[4][3] = int(self.cB43.currentText())
        self.matrix[4][4] = int(self.cB44.currentText())
        self.matrix[4][5] = int(self.cB45.currentText())
        self.matrix[4][6] = int(self.cB46.currentText())
        self.matrix[4][7] = int(self.cB47.currentText())
        self.matrix[4][8] = int(self.cB48.currentText())

        self.matrix[5][0] = int(self.cB50.currentText())
        self.matrix[5][1] = int(self.cB51.currentText())
        self.matrix[5][2] = int(self.cB52.currentText())
        self.matrix[5][3] = int(self.cB53.currentText())
        self.matrix[5][4] = int(self.cB54.currentText())
        self.matrix[5][5] = int(self.cB55.currentText())
        self.matrix[5][6] = int(self.cB56.currentText())
        self.matrix[5][7] = int(self.cB57.currentText())
        self.matrix[5][8] = int(self.cB58.currentText())

        self.matrix[6][0] = int(self.cB60.currentText())
        self.matrix[6][1] = int(self.cB61.currentText())
        self.matrix[6][2] = int(self.cB62.currentText())
        self.matrix[6][3] = int(self.cB63.currentText())
        self.matrix[6][4] = int(self.cB64.currentText())
        self.matrix[6][5] = int(self.cB65.currentText())
        self.matrix[6][6] = int(self.cB66.currentText())
        self.matrix[6][7] = int(self.cB67.currentText())
        self.matrix[6][8] = int(self.cB68.currentText())

        self.matrix[7][0] = int(self.cB70.currentText())
        self.matrix[7][1] = int(self.cB71.currentText())
        self.matrix[7][2] = int(self.cB72.currentText())
        self.matrix[7][3] = int(self.cB73.currentText())
        self.matrix[7][4] = int(self.cB74.currentText())
        self.matrix[7][5] = int(self.cB75.currentText())
        self.matrix[7][6] = int(self.cB76.currentText())
        self.matrix[7][7] = int(self.cB77.currentText())
        self.matrix[7][8] = int(self.cB78.currentText())

        self.matrix[8][0] = int(self.cB80.currentText())
        self.matrix[8][1] = int(self.cB81.currentText())
        self.matrix[8][2] = int(self.cB82.currentText())
        self.matrix[8][3] = int(self.cB83.currentText())
        self.matrix[8][4] = int(self.cB84.currentText())
        self.matrix[8][5] = int(self.cB85.currentText())
        self.matrix[8][6] = int(self.cB86.currentText())
        self.matrix[8][7] = int(self.cB87.currentText())
        self.matrix[8][8] = int(self.cB88.currentText())

    
    def output(self):
        self.lcd00.display(int(self.matrix[0][0]))
        self.lcd01.display(int(self.matrix[0][1]))
        self.lcd02.display(int(self.matrix[0][2]))
        self.lcd03.display(int(self.matrix[0][3]))
        self.lcd04.display(int(self.matrix[0][4]))
        self.lcd05.display(int(self.matrix[0][5]))
        self.lcd06.display(int(self.matrix[0][6]))
        self.lcd07.display(int(self.matrix[0][7]))
        self.lcd08.display(int(self.matrix[0][8]))

        self.lcd10.display(int(self.matrix[1][0]))
        self.lcd11.display(int(self.matrix[1][1]))
        self.lcd12.display(int(self.matrix[1][2]))
        self.lcd13.display(int(self.matrix[1][3]))
        self.lcd14.display(int(self.matrix[1][4]))
        self.lcd15.display(int(self.matrix[1][5]))
        self.lcd16.display(int(self.matrix[1][6]))
        self.lcd17.display(int(self.matrix[1][7]))
        self.lcd18.display(int(self.matrix[1][8]))

        self.lcd20.display(int(self.matrix[2][0]))
        self.lcd21.display(int(self.matrix[2][1]))
        self.lcd22.display(int(self.matrix[2][2]))
        self.lcd23.display(int(self.matrix[2][3]))
        self.lcd24.display(int(self.matrix[2][4]))
        self.lcd25.display(int(self.matrix[2][5]))
        self.lcd26.display(int(self.matrix[2][6]))
        self.lcd27.display(int(self.matrix[2][7]))
        self.lcd28.display(int(self.matrix[2][8]))

        self.lcd30.display(int(self.matrix[3][0]))
        self.lcd31.display(int(self.matrix[3][1]))
        self.lcd32.display(int(self.matrix[3][2]))
        self.lcd33.display(int(self.matrix[3][3]))
        self.lcd34.display(int(self.matrix[3][4]))
        self.lcd35.display(int(self.matrix[3][5]))
        self.lcd36.display(int(self.matrix[3][6]))
        self.lcd37.display(int(self.matrix[3][7]))
        self.lcd38.display(int(self.matrix[3][8]))

        self.lcd40.display(int(self.matrix[4][0]))
        self.lcd41.display(int(self.matrix[4][1]))
        self.lcd42.display(int(self.matrix[4][2]))
        self.lcd43.display(int(self.matrix[4][3]))
        self.lcd44.display(int(self.matrix[4][4]))
        self.lcd45.display(int(self.matrix[4][5]))
        self.lcd46.display(int(self.matrix[4][6]))
        self.lcd47.display(int(self.matrix[4][7]))
        self.lcd48.display(int(self.matrix[4][8]))
        
        self.lcd50.display(int(self.matrix[5][0]))
        self.lcd51.display(int(self.matrix[5][1]))
        self.lcd52.display(int(self.matrix[5][2]))
        self.lcd53.display(int(self.matrix[5][3]))
        self.lcd54.display(int(self.matrix[5][4]))
        self.lcd55.display(int(self.matrix[5][5]))
        self.lcd56.display(int(self.matrix[5][6]))
        self.lcd57.display(int(self.matrix[5][7]))
        self.lcd58.display(int(self.matrix[5][8]))

        self.lcd60.display(int(self.matrix[6][0]))
        self.lcd61.display(int(self.matrix[6][1]))
        self.lcd62.display(int(self.matrix[6][2]))
        self.lcd63.display(int(self.matrix[6][3]))
        self.lcd64.display(int(self.matrix[6][4]))
        self.lcd65.display(int(self.matrix[6][5]))
        self.lcd66.display(int(self.matrix[6][6]))
        self.lcd67.display(int(self.matrix[6][7]))
        self.lcd68.display(int(self.matrix[6][8]))

        self.lcd70.display(int(self.matrix[7][0]))
        self.lcd71.display(int(self.matrix[7][1]))
        self.lcd72.display(int(self.matrix[7][2]))
        self.lcd73.display(int(self.matrix[7][3]))
        self.lcd74.display(int(self.matrix[7][4]))
        self.lcd75.display(int(self.matrix[7][5]))
        self.lcd76.display(int(self.matrix[7][6]))
        self.lcd77.display(int(self.matrix[7][7]))
        self.lcd78.display(int(self.matrix[7][8]))

        self.lcd80.display(int(self.matrix[8][0]))
        self.lcd81.display(int(self.matrix[8][1]))
        self.lcd82.display(int(self.matrix[8][2]))
        self.lcd83.display(int(self.matrix[8][3]))
        self.lcd84.display(int(self.matrix[8][4]))
        self.lcd85.display(int(self.matrix[8][5]))
        self.lcd86.display(int(self.matrix[8][6]))
        self.lcd87.display(int(self.matrix[8][7]))
        self.lcd88.display(int(self.matrix[8][8]))


class SudokuSolver:
    def __init__(self, input_matrix):
        self.arr = input_matrix
        self.pos = {}
        self.rem = {}
        self.graph = {}
        self.build_pos_and_rem()
        self.build_graph()

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
        return self.arr


def main():

    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()