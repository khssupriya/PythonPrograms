def dig(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def look_and_say(n):
    if dig(n) % 2 == 1:
        return "invalid"
    s = str(n)
    res = ""
    i = 0
    while i < len(s):
        res += s[i+1]*int(s[i])
        i += 2
    return int(res)