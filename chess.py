def is_valid_move(s, color):
    try:
        piece, start, end = s.split()
    except:
        pawn(s, color)
    horizontal = abs(ord(start[0]) - ord(end[0]))
    vertical = abs(ord(start[1]) - ord(end[1]))
    if piece == "K":
        return horizontal <= 1 and vertical <= 1
    elif piece == "Q":
        return horizontal==0 or vertical==0 or horizontal == vertical
    elif piece == "B":
        return horizontal == vertical
    elif piece == "R":
        return horizontal==0 or vertical==0
    elif piece == "N":
        return horizontal,vertical in [(1,2), (2,1)]

print(is_valid_move("N e3 d5", "Black"))

def pawn(s, color):    
    start, end = s.split()
    horizontal = ord(start[0]) - ord(end[0])
    vertical = ord(start[1]) - ord(end[1])
    if horizontal != 0:
        return False
    else:
        if vertical == 1:
            return True
        elif vertical == 2:
            if color == "Black":
                return start[1] == '7'
            else:
                return start[1] =='2'  
        else:
            return False