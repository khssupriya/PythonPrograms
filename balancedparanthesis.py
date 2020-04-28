def SplitParenthesis(s):
    splitlist = []
    stack = []
    prev = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            stack.pop()
        if len(stack) == 0:
            splitlist.append(s[prev:i+1])
            prev = i+1
    return splitlist