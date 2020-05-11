from PGNPreProcess import *
import CheckValidMove

SPACE = " "

pawn_can_move_from = {"P": {"3":"2","4":["3","2"],"5":"4","6":"7","8":"7"},
                      "p": {"6":"7","5":["6","7"],"4":"5","3":"4","2":"3","1":"2"}}

def is_regular_pawn():
    



def get_from_pos(COLOR, piece, to_pos):
    possible_pieces = piece_view[piece]
    for pos in possible_pieces:
        if piece.upper() != "P" and CheckValidMove.check_piece_move(piece, pos, to_pos):
            return pos
        elif CheckValidMove.check_pawn_move(COLOR, pos, to_pos):
            return pos

def update_pos(COLOR, piece, to_pos):
    from_pos = get_from_pos(COLOR, piece, to_pos)
    board_view[from_pos]=" "
    piece_view[piece].remove(from_pos)
    piece_view[piece].append(to_pos)
    board_view[to_pos]=piece

# def king_castle(COLOR, king, rook):
#     update_pos(COLOR, king, )
#     update_pos(COLOR, rook, )

# def queen_castle(COLOR, king, rook):
#     update_pos(COLOR, king)
#     update_pos(COLOR, rook, get_from_pos(king, get_from_pos(king)[0] + str(int(get_from_pos(king)[1])-1)))

def castle(COLOR, move):
    king = {"WHITE": "K", "BLACK": "k"}[COLOR]
    rook = {"WHITE": "R", "BLACK": "r"}[COLOR]
    #{"o-o":king_castle, "o-o-o": queen_castle}[move.lower()](COLOR, king, rook)

def capture(position):
    piece = board_view[position]
    board_view[position]=" "
    piece_view[piece].remove(position)

def is_check(move):
    return move[-1] == "+"

def make_piece_move(COLOR, move):
    if is_check(move):
        piece, destination, extra = move[0], move[1:-1], move[-1:]
    else:
        piece, extra, destination = move[0], move[1:-2], move[-2:]
    if extra == "x":
        capture(destination)
    update_pos(COLOR, piece, destination)

def is_enpassant(move):
    return False

def make_enpassant(COLOR,move):
    pass

def make_pawn_move(move):
    if is_

def make_one_move(move):
    if move[0] in"pP":
        make_pawn_move(move)
    elif move[0] in "oO":
        make_castling(move)
    else:
        make_piece_move(move)
    
def make_moves(pgnfile):
    # if not os.path.exists(pgnfile):
    #     print(f"PGN file {pgnfile} not found")
    #     exit(1)
    for wmove,bmove in MOVES[:-1]:
        make_one_move(wmove)
        make_one_move(bmove)
    if len(MOVES[-1])==2:
        wmove, bmove = MOVES[-1]
        make_one_move(wmove)
        make_one_move(bmove)
    else:
        wmove = MOVES[-1]
        make_one_move(wmove)
    #display_board()
    exit(0)

if __name__ == "__main__":
    board_view, piece_view = setup()
    make_moves("chessgame.py")
    





