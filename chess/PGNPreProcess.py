import re

def setup():
    squares = [y+x for y in "abcdefgh" for x in "12345678"]
    start = "RNBQKBNR" + "P"*8 + " "*32 + "p"*8 + "rnbkqbnr"
    board_view = {square: piece for square, piece in zip(squares, start)} #keeps track of all the squares in the board
    piece_view = {_:[] for _ in "BKNPQRbknpqr"} #keeps track of the positions of pieces only ( i.e, except empty squares)
    for sq in board_view:
        piece = board_view[sq]
        if piece != ' ':
            piece_view[piece].append(sq)
    return board_view, piece_view

def pgn_to_moves(game_file:str)->[str]:
    raw_pgn = " ".join([line.strip() for line in open(game_file)])

    # Pre-process to remove comments to enable regex
    # Remove comments == text with in {}

    comments_marked = raw_pgn.replace('{', '<').replace('}','>')
    STRC = re.compile("<[^>]*>")
    comments_removed = STRC.sub(" ",comments_marked)

    # Pre-process STR to enable regex
    #Remove STR == text within []

    STR_marked = comments_removed.replace("[", "<").replace("]", ">")
    str_removed = STRC.sub(" ",STR_marked)

    # Remove move numbers

    MOVE_NUM = re.compile('[1-9][0-9]* *\\.')
    just_moves = [_.strip() for _ in MOVE_NUM.split(str_removed)]

    #Remove final result

    last_move = just_moves[-1]
    RESULT = re.compile('( *1 *-*0| *0 *-*1| *1/2 *-*1/2)')
    last_move = RESULT.sub(" ",last_move)
    #print(last_move)
    moves = just_moves[:-1] + [last_move]

    return [_ for _ in moves if len(_) > 0]

def pre_process_a_move(move: str)->(str, str):
    wmoves, bmoves = move.split()
    if wmoves[0] in "abcdefgh":
        wmoves = "P" + wmoves
    if bmoves[0] in "abcdefgh":
        bmoves = "p" + bmoves
    else:
        bmoves = bmoves.lower()
    return wmoves, bmoves

def pre_process_moves(moves):
    return [pre_process_a_move(move) for move in moves]

MOVES = pre_process_moves(pgn_to_moves("chessgame.pgn"))