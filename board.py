from side_modules.linked_binary_tree import LinkedBinaryTree


class Board:
    def __init__(self):
        self.board = [['0', '0', '0'],
                      ['0', '0', '0'],
                      ['0', '0', '0']]
        self.last_move = []

    @staticmethod
    def check_win(board):
        for i in range(3):
            if (board[i][0] == board[i][1]) and (
                    board[i][0] == board[i][2]) and (
                    board[i][0] != '0'):
                return True, board[i][0]
            if (board[0][i] == board[1][i]) and (
                    board[0][i] == board[2][i]) and (
                    board[i][0] != '0'):
                return True, board[0][i]
        if (board[0][0] == board[1][1]) and (
                board[0][0] == board[2][2]) and (
                board[0][0] != '0'):
            return True, board[0][0]
        if (board[0][2] == board[1][1]) and (
                board[0][2] == board[2][0]) and (
                board[0][0] != '0'):
            return True, board[0][2]
        return False

    def recurs_tree_generation(self, tr, player_char):
        left_vertex = self.generate_move(tr.key, player_char)
        if left_vertex is not None:
            tr.insert_left(left_vertex)
            if player_char == 'z':
                self.recurs_tree_generation(tr.get_left_child(), 'x')
            else:
                self.recurs_tree_generation(tr.get_left_child(), 'z')
        right_vertex = self.generate_move(tr.key, player_char, left_vertex)
        if right_vertex is not None:
            tr.insert_right(right_vertex)
            if player_char == 'z':
                self.recurs_tree_generation(tr.get_right_child(), 'x')
            else:
                self.recurs_tree_generation(tr.get_right_child(),  'z')

    def generate_tree(self, board, player_char):
        tr = LinkedBinaryTree(board)
        self.recurs_tree_generation(tr, player_char)
        print(tr.get_right_child())
        return tr

    def count_points(self, tree, chr_1, chr_2):
        def rec_count(vertex):
            if vertex is None:
                return 0
            for row_ind in vertex.key:
                if "0" in vertex.key[row_ind]:
                    return rec_count(vertex.get_left_child()) + \
                           rec_count(vertex.get_right_child())
            check_rez = self.check_win(vertex.key)[0]
            if check_rez[0] and check_rez[1] == chr_1:
                return 1
            elif check_rez[0] and check_rez[1] == chr_2:
                return -1
            return 0
        return rec_count(tree)

    def move(self, chr_1, chr_2):
        tree = self.generate_tree(self.board, chr_1)
        print(tree)
        if self.count_points(tree.get_left_child(), chr_1, chr_2) >= \
                self.count_points(tree.get_right_child(), chr_1, chr_2):
            self.board = tree.get_left_child().key
        else:
            self.board = tree.get_right_child().key

    @staticmethod
    def check_eq(brd_1, brd_2):
        for i in range(2):
            for j in range(2):
                if brd_1.element()[i][j] != brd_2.element()[i][j]:
                    return False
        return True

    def generate_move(self, board, player_char, already_generated=None):
        for i in range(3):
            for j in range(3):
                if board[i][j] == '0':
                    board[i][j] = player_char
                    if already_generated is not None and not self.check_eq(board, already_generated):
                        return board
                    elif already_generated is None:
                        return board


if __name__ == "__main__":
    gm = Board()
    print(gm.board)
    gm.generate_tree(gm.board, 'z').get_right_child()
    print(gm.move('z', 'x'))
