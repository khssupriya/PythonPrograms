def pick10(s: str, n:int) -> str:
    l = len(s)
    visited =""
    i = 1
    n = n%l
    while len(visited) != 10:
        visited += s[n]
        n = (n + i)%l
        i += 1
    return visited
print(pick10( "ABC", 1))