def is_king_checked(board):
    """
    Checks if the King ('K') is in check on a chessboard.
    :param board: List of strings representing rows of the chessboard.
    :return: True if the King is in check, False otherwise.
    """
    n = len(board)
    king_positions = [(i, row.index('K')) for i, row in enumerate(board) if 'K' in row]

    # Ensure there's exactly one King
    if len(king_positions) != 1:
        raise ValueError("Invalid board: there must be exactly one King")

    kx, ky = king_positions[0]

    def is_in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    pawn_dirs = [(1, 1), (1, -1)]
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queen_dirs = bishop_dirs + rook_dirs

    for dx, dy in pawn_dirs:
        nx, ny = kx + dx, ky + dy
        if is_in_bounds(nx, ny) and board[nx][ny] == 'P':
            return True

    for piece, directions in [('B', bishop_dirs), ('R', rook_dirs), ('Q', queen_dirs)]:
        for dx, dy in directions:
            x, y = kx, ky
            while True:
                x, y = x + dx, y + dy
                if not is_in_bounds(x, y):
                    break
                if board[x][y] == piece:
                    return True
                elif board[x][y] != '.':
                    break

    return False
