def isprime(n):
    if n == 1:
        return False
    if n in [2,3,5,7]:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def digits(n):
    dig = []
    while n>0:
        dig.append(n%10)
        n //= 10
    return dig

def isharshad(n):
    return n%sum(digits(n)) == 0

def ismoran(n):
    return isprime(n//sum(digits(n)))

def moranNumbers(n):
    if not isharshad(n):
        return "Neither"
    if ismoran(n):
        return "M"
    return "H"