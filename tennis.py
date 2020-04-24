SCORING = {0:0,1:15,2:30,3:40}

scores={"A":0,"B":0}
games={"A":0,"B":0}
sets={"A":0,"B":0}

def setscrores():
    scores["A"]=scores["B"]=0

def setgames():
    games["A"]=games["B"]=0

def isdeuce():
    return scores["A"]==3 and scores["B"]==3

def isgame():
    return scores["A"]==4 or scores["B"]==4

def isset():
    return games["A"]==6 or games["B"]==6

def handle_deuse(AB_str):
    setscrores()
    AD={"A":0,"B":0}
    for i in range(len(AB_str)):
        AD[AB_str[i]]+=1
        if AD[AB_str[i]]==2:
            games[AB_str[i]]+=1
            return i+1
    return 0

def handle_game():
    if scores["A"]==4:
        games["A"]+=1
    else:
        games["B"]+=1
    setscrores()

def handle_set():
    if games["A"]==6:
        sets["A"]+=1
    else:
        sets["B"]+=1
    setgames()

def calc_score(AB_str):
    i=0
    while i<len(AB_str):
        scores[AB_str[i]]+=1
        if isdeuce():
            i+=handle_deuse(AB_str[i+1:])+1
        else:
            i+=1
        if isgame():
            handle_game()
        if isset():
            handle_set()
    scores["A"]=SCORING[scores["A"]]
    scores["B"]=SCORING[scores["B"]]
    return {"scores":scores,"games":games,"sets":sets}

print(calc_score("ABABABAAB"))
