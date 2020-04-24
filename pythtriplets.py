def pythagoreanTriplets(n):
    count = 0
    for a in range(1, n//3 +1):
        for b in range(a+1, n//2 +1):
            c = n - a - b
            if a*a + b*b == c*c:
                count +=1
    return count
                    
def peri() -> int:
    res = [pythagoreanTriplets(i) for i in range(12, 1000)]
    return res.index(max(res))
    
print(peri())