BOARD = [x + y for x in "ABCDEFGH" for y in "12345678"]
HOME = {"WHITE":2,"BLACK":7}

def file_diff(from_pos: str, to_pos: str) -> int:
    return abs(ord(from_pos[0]) - ord(to_pos[0]))


def rank_diff(from_pos: str, to_pos: str) -> int:
    return abs(ord(from_pos[1]) - ord(to_pos[1]))


def move_sep(from_pos: str, to_pos: str) -> (int, int):
    return file_diff(from_pos, to_pos), rank_diff(from_pos, to_pos), 


def check_piece_move(piece: str, from_pos: str, to_pos: str) -> bool:
    fp = from_pos.strip().upper()
    tp = to_pos.strip().upper()
    if fp == tp or from_pos not in BOARD or to_pos not in BOARD:
        return False
    moved_by = move_sep(fp, tp)
    
    def can_rook_move():
        return moved_by[0] == 0 or moved_by[1] == 0

    def can_knight_move():
        return moved_by in [(1, 2), (2, 1)]
    
    def can_bishop_move():
        return moved_by[0] == moved_by[1]

    def can_queen_move():
        return can_rook_move() or can_bishop_move()

    def can_king_move():
        return moved_by in [(0, 1), (1, 0), (1, 1)]

    return {"R": can_rook_move, "N": can_knight_move,  "B": can_bishop_move, "Q": can_queen_move, "K": can_king_move}[piece.upper()]()

def check_pawn_move(COLOR, from_pos: str,to_pos: str):
    fp = from_pos.strip().upper()
    tp = to_pos.strip().upper()
    if fp == tp or from_pos not in BOARD or to_pos not in BOARD:
        return False
    moved_by = move_sep(fp, tp)
    return moved_by[0] == 0 and ((from_pos[1] == HOME[COLOR] and moved_by[1] <= 2) or  moved_by[1] == 1)

if __name__=="__main__":
    print(check_pawn_move("WHITE", "A3", "A4"))

