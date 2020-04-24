def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

def is_triplet(a, b, c):
    return a ** 2 + b ** 2 == c** 2 or b ** 2 + c ** 2 == a** 2 or  c** 2 + a ** 2 == b** 2

def primitive_pyth() -> [(int, int, int)]:
    ans=list()
    for a in range(1, 100):
        for b in range(a+1, 100):
            for c in range(b+1,100):
                if is_triplet(a,b,c):
                    if gcd(a,b) == 1 or gcd(b,c) == 1 or gcd(c,a) == 1:
                        ans.append((a,b,c))
                    elif gcd(a,b) != gcd(b,c):
                        ans.append((a,b,c))
    return ans
print(primitive_pyth()) 