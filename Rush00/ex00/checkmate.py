def is_king_checked(board):
    """
    Checks if the King ('K') is in check on a chessboard.
    :param board: List of strings representing rows of the chessboard.
    """
    n = len(board)  # Size of the board (n x n)
    
    # Locate the King's position
    king_pos = None
    for i, row in enumerate(board):
        if 'K' in row:
            king_pos = (i, row.index('K'))
            break
    
    if not king_pos:
        print("error: No King found")
        return
    
    kx, ky = king_pos
    
    def is_in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    # Directions for Pawns, Bishops, Rooks, and Queens
    pawn_dirs = [(1, 1), (1, -1)]  # Pawns attack diagonally forward
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonals
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Horizontal & vertical
    queen_dirs = bishop_dirs + rook_dirs  # Queen combines Bishop and Rook
    
    # Check for Pawn threats
    for dx, dy in pawn_dirs:
        nx, ny = kx + dx, ky + dy
        if is_in_bounds(nx, ny) and board[nx][ny] == 'P':
            print("Success")
            return
    
    # Check for sliding pieces (Bishops, Rooks, Queens)
    for piece, directions in [('B', bishop_dirs), ('R', rook_dirs), ('Q', queen_dirs)]:
        for dx, dy in directions:
            x, y = kx, ky
            while True:
                x, y = x + dx, y + dy
                if not is_in_bounds(x, y):
                    break
                if board[x][y] == piece:
                    print("Success")
                    return
                elif board[x][y] != '.':  # Blocked by another piece
                    break
    
    # No threat detected
    print("Fail")