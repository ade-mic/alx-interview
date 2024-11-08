#!/usr/bin/python3
"""
The N-Queens problem is a classic example of a backtracking algorithm.
The goal is to place N queens on an (N x N) chessboard such
that no two queens threaten each other.
This means no two queens can share the same row, column, or diagonal.
"""
import sys


def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns all possible solutions.

    Args:
    n (int): The number of queens and the size of the chessboard (n x n).

    Returns:
    List[List[List[int]]]: A list of solutions, where each solution is
    represented as a list of lists. Each inner list contains
    two integers representing the row and column of a queen.
    """

    def is_safe(board, row, col):
        """
        Checks if it's safe to place a queen at board[row][col].

        Args:
        board (List[int]): The current state of the chessboard.
        row (int): The row index.
        col (int): The column index.

        Returns:
        bool: True if it's safe to place the queen, False otherwise.
        """
        # Check column conflicts
        for i in range(row):
            if board[i] == col:
                return False
        # Check diagonal conflicts
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row, board):
        """
        Recursively attempts to place queens on the board.

        Args:
        board (List[int]): The current state of the chessboard.
        row (int): The current row to place a queen.
        """
        if row == n:
            result.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1  # Reset the row to its initial state

    result = []
    board = [-1] * n  # Use a 1D array to store column positions of queens
    solve(0, board)
    return result


def main():
    """Main script to call the algorithm."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
