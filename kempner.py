primes = list()

def sieves(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*2,n+1,p):
                prime[i] = False
        p += 1
    prime[0] = prime[1] = False
    for p in range(n+1):
        if prime[p]:
            primes.append(p)
        
def prime_factors(num):
    if num == 1:
        return [(1,1)]
    ans = []
    for p in primes:
        if p > num:
            break
        count = 0
        while num % p == 0:
            num //= p
            count += 1
        if count > 0:
            ans.append((p, count))
    return ans

def fun(num, freq):
    if freq > num:
        return num*(freq-1)
    else:
        return num*freq

def kempner(n):
    sieves(n+2)
    if n == 1:
        return 1
    if n in primes:
        return n
    return max(fun(x,y) for x,y in prime_factors(n))