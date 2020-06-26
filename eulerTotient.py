import matplotlib.pyplot as plt 

def totient(n): 
    phi = n
    p = 2 
    while(p * p <= n):
        while (n % p == 0): 
            n = n // p
        phi -= phi // p
        p += 1
    if (n > 1): 
        phi -= phi // n
    return phi

x = []
y = []
for i in range(1,1000):
    x.append(i)
    y.append(totient(i))

plt.scatter(x, y, c ="blue") 
plt.show() 