import numpy as np 
import matplotlib.pyplot as plt  
from collections import defaultdict 

def def_value(): 
    return 0

f = open("gameoflifefinal.py", "r")
str = f.read()
data = defaultdict(def_value) 
for each in str:
    if ord(each.lower()) in range(97,123):
        data[each.lower()] += 1
print(data)

courses = list(data.keys()) 
values = list(data.values()) 
   
fig = plt.figure(figsize = (10, 5)) 

plt.bar(courses, values, color ='maroon', width = 0.4)   
plt.xlabel("Aplphabet") 
plt.ylabel("Frequency") 
plt.title("Aphabet Frequency") 
plt.show() 
