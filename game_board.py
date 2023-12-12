from tabulate import tabulate
import copy


class Board:
    def __init__(self, m: int, n: int) -> None:
        self.rows = m
        self.columns = n
        self.board = [['0']*n for i in range(0, m, 1)]

    def print_board(self) -> None:
        print(tabulate(self.board, tablefmt="fancy_grid"))

    def special_print(self, table1=None, table2=None, table3=None) -> None:
        tables_and_strings = []

        for table in [table1, table2, table3]:
            if table is not None:
                table_str = tabulate(table, tablefmt="fancy_grid")
                lines = table_str.split('\n')
                tables_and_strings.append((table, lines))

        if not tables_and_strings:
            return

        max_lines = max(len(lines) for _, lines in tables_and_strings)

        combined_lines = []
        for i in range(max_lines):
            combined_line = "   ".join(lines[i] if i < len(
                lines) else '' for _, lines in tables_and_strings)
            combined_lines.append(combined_line)

        result = '\n'.join(combined_lines)
        print(result, end='\n\n')

        return

    def check_boundary_conditions(self, x, y) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.columns

    def check_win_state(self) -> int:
        temp = []

        for row in self.board:
            for x in row:
                temp.append(x)

        opt_1 = [x for x in temp if '1' in x]
        opt_2 = [x for x in temp if '2' in x]

        if len(opt_1) == 0 and len(opt_2) > 1:
            return 2
        elif len(opt_2) == 0 and len(opt_1) > 1:
            return 1

        return 0

    def perform_chain_reaction(self, is_print: bool = True) -> None:
        if is_print == True:
            self.print_board()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        locs = [[i, j] for i in range(self.rows) for j in range(
            self.columns) if len(self.board[i][j]) >= 3]

        while len(locs) != 0:
            i, j = locs[0]
            locs.pop(0)

            self.board[i][j] = self.board[i][j][0]
            for x, y in directions:
                if self.check_boundary_conditions(i+x, j+y):
                    if self.board[i+x][j+y][0] == self.board[i][j][0]:
                        self.board[i+x][j+y] += self.board[i][j][0]
                    else:
                        self.board[i+x][j+y] = self.board[i][j][0]

                    if len(self.board[i+x][j+y]) >= 3:
                        locs.append([i+x, j+y])

        if is_print == True:
            self.print_board()
        return
