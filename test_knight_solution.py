import unittest
from knight_solution import Chessboard, Knight, get_possible_moves, shortest_path, chess_notation_to_position

class TestKnightSolution(unittest.TestCase):
    """
    Test cases for the knight's shortest path solution.

    Methods:
        test_chess_build_chessboard: Test if build_chessboard function creates a valid chessboard.
        test_valid_position: Test if Knight.can_move returns True for valid positions.
        test_invalid_position: Test if Knight.can_move returns False for invalid positions.
        test_possible_moves: Test if get_possible_moves returns the correct possible moves for a given position.
        test_shortest_path: Test if shortest_path returns the correct shortest path between two positions.
        test_chess_notation_to_position: Test if chess_notation_to_position converts chess notation to position correctly.
    """

    def test_chess_build_chessboard(self):
        """
        Test if build_chessboard function creates a valid chessboard.

        Asserts:
            - The shape of the chessboard is (8, 8).
        """
        chessboard = Chessboard.build(4, 4)
        self.assertEqual(chessboard.shape, (8, 8))

    def test_valid_position(self):
        """
        Test if Knight.can_move returns True for valid positions.
        """
        valid_position = [(0, 0), (1, 2),(2, 0), (3, 2), (4, 0),(7,7)]
        for row, col in valid_position:
            self.assertTrue(Knight.can_move(row, col)) 

    def test_invalid_position(self):
        """
        Test if Knight.can_move returns False for invalid positions.
        """
        invalid_positions = [
            (-1, 3), (8, 5), (2, 9), (10, -3),
            (0, 8), (7, -1), (-1, -1), (8, 8)
        ]
        for row, col in invalid_positions:
            self.assertFalse(Knight.can_move(row, col), f"Position ({row}, {col}) should be invalid.")

    def test_possible_moves(self):
        """
        Test if get_possible_moves returns the correct possible moves for a given position.

        Asserts:
            - The possible moves match the expected moves for the starting position (0, 0).
        """
        possible_moves = get_possible_moves((0, 0))
        expected_moves = [(1, 2), (2, 1)]
        self.assertEqual(possible_moves, expected_moves)
        
    def test_shortest_path(self):
        """
        Test if shortest_path returns the correct shortest path between two positions.

        Asserts:
            - The shortest path matches the expected path between the start and end positions.
        """
        start = (0, 0)
        end = (7, 7)
        path = shortest_path(start, end)
        expected_path = [[(0, 0), (1, 2), (2, 4), (3, 6), (4, 4), (5, 6), (7, 7)]]
        self.assertEqual(path, expected_path)

    def test_chess_notation_to_position(self):
        """
        Test if chess_notation_to_position converts chess notation to position correctly.

        Asserts:
            - The converted position matches the expected position for 'A1'.
        """
        position = chess_notation_to_position('A1')
        expected_position = (0, 0)
        self.assertEqual(position, expected_position)

if __name__ == '__main__':
    unittest.main()
