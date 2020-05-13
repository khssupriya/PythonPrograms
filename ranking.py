import itertools as it
import os
from sys import argv 

def relation(A, B):
    metric = sum([int(a >= b) for a, b in zip(A, B)])
    if metric == len(A):
        return ">"
    elif metric == 0:
        return "<"
    else:
        return "#"

matrix = {}
for line in open(argv[1]):
    marks = line.strip().split()
    matrix[marks[0]] = [int(x) for x in marks[1:]]

keys = list(matrix.keys())
combo = it.combinations(keys, 2)
rels = set([])
for key1, key2 in combo:
    r = relation(matrix[key1], matrix[key2])
    if r == ">":
        rels.add(key1 + key2)
    elif r == "<":
        rels.add(key2 + key1)

rels = list(sorted(rels))

start = set([x[0] for x in rels])
ends = set([x[1] for x in rels])
both = start & ends

removables = set([])
rules = set([])
for x in start:
    for y in ends:
        if x + y not in rels:
            continue
        for z in both:
            if x + z in rels and z + y in rels:
                removables.add(x+y)
                rules.add(x+y + " <= " + x+z + " & " + z+y  )
print("ALL relations\n", rels)
print("Removables   \n", list(sorted(removables)))
print("Removal rules\n", list(sorted(rules)))
print("Minimal      \n", list(sorted(set(rels)^removables)))
minimal = sorted(set(rels) ^ removables)

start = [x[0] for x in minimal]
ends = [x[1] for x in minimal]
temp = []

for x in start:
    if not x in ends:
        temp.append(x)

def find_here(s, ch):
    for i in range(len(s)-1):
        if s[i] == ch and s[i+1] == "$":
            return i
        if s[-1] == ch:
            return len(s)-1
    return -2

s = "$".join(temp)
while True:
    f = 0
    for each in minimal:
        if not each in s:
            pos = find_here(s, each[0])
            if pos == -2:
                continue
            f = 1
            if pos != len(s) - 2: 
                s = s[:pos+1] + each[1] + s[pos+1:]
            else:
                s += each[1]
    if f == 0:
        break

partial_ranked = '>'.join(ch for ch in s) 
partial_ranked = partial_ranked.replace(">$>","\n")

print("FINAL RESULT\n", partial_ranked)


with open("vanchi.dot", "w") as f:
    print("digraph vanchi {", file=f)
    for relation in minimal:
        print("\t%s -> %s;" %(relation[0], relation[1]), file=f)
    print("}", file=f)

os.system("dot -T png -o vanchi.png vanchi.dot")
