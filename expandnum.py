def expand(num):
    if num == 0:
        return 0
    dig = list()
    exp = ""
    while num > 0:
        dig.append(num%10)
        num //= 10
    dig.reverse()
    power = len(dig) - 1
    for x in dig:
        if x != 0:
            exp += str(x*pow(10,power)) + " + "
        power -= 1
    return exp[:-3]
print(expand(1103))