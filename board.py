from linked_binary_tree import LinkedBinaryTree


class Board:
    def __init__(self):
        self.board = [['0', '0', '0'],
                      ['0', '0', '0'],
                      ['0', '0', '0']]
        self.last_move = []

    def check_win(self):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1]) and (
                    self.board[i][0] == self.board[i][2]) and (
                    self.board[i][0] != '0'):
                return True
            if (self.board[0][i] == self.board[1][i]) and (
                    self.board[0][i] == self.board[2][i]) and (
                    self.board[i][0] != '0'):
                return True
        if (self.board[0][0] == self.board[1][1]) and (
                self.board[0][0] == self.board[2][2]) and (
                self.board[0][0] != '0'):
            return True
        if (self.board[0][2] == self.board[1][1]) and (
                self.board[0][2] == self.board[2][0]) and (
                self.board[0][0] != '0'):
            return True
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
        return tr

    @staticmethod
    def count_points(tree):
        pass

    def move(self):
        tree = self.generate_tree(self.board, 'z')

        # countinng_rez = self.count_points(tree)
        #
        # if countinng_rez[0] > countinng_rez[1]:
        #     return tree.left
        # else:
        #     return tree.right
        return tree

    @staticmethod
    def check_eq(brd_1, brd_2):
        for i in range(2):
            for j in range(2):
                if brd_1.element()[i][j] != brd_2.element()[i][j]:
                    return False
        return True

    def generate_move(self, board, player_char, already_generated=None):
        for i in range(2):
            for j in range(2):
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

