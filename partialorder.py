from collections import defaultdict

def rank_students(report):
    is_greater = [[0]*100]*1000
    for roll1 in report:
        for roll2 in report:
            if roll1 != roll2:
                count = 0
                for x in report[roll1] - report[roll2]:
                    if x>0:
                        count +=1
                if count == 3:
                    is_greater[roll1,roll2] = 1
    return "a>b>c"

def pre_process(file_name):
    raw_file = [line.strip() for line in open(file_name)]
    d = defaultdict()
    for line in raw_file:
        d[line[0]]=line[2:].split(" ")
    return d

print(rank_students(pre_process("studentmarks.txt")))