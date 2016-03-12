__author__ = 'anurag'

import pandas as pd
import numpy as np
import gzip, csv
from math import pow

class club:
    def __init__(self,category,district,days):
        self.Day = days
        self.category = category
        self.PdDistrict = district

def Comp(a,b):
    if b.category > a.category:
        return 1
    else:
        return 0


class TestClub:
    def __init__(self,district,days):
        self.Day = days
        self.PdDistrict = district
def Sim(a,b):
    d = 0
    if a.PdDistrict == b.PdDistrict:
        d += 1
    if a.Day == b.Day:
        d += 1
    return d
def MaxCat(n):
    n.sort(Comp)
    maxc = 1
    maxcat = n[0].category
    p = 1
    for i in range(1,len(n)):
        if n[i].category ==n[i-1].category:
            p+=1
        else:
            p = 1
            if p > maxc:
                maxc = p
                maxcat = n[i-1].category

    return maxcat
train = pd.read_csv("train.csv")
N = float(len(train))
Days = np.array(train['DayOfWeek'])
pdDistricts = (np.array(train['PdDistrict']))
classes = sorted((np.unique(train['Category'])))
Categories = np.array(train['Category'])
Sol = ['Id']
Sol += classes

test = pd.read_csv(r'test.csv')
outf = gzip.open(r'Output.csv.gz', 'wt')
fo = csv.writer(outf, lineterminator='\n')
fo.writerow(Sol)
counter = 0
for (idd, dist, day) in zip(test['Id'], test['PdDistrict'], test['DayOfWeek']):
    sol = [idd]
    n = []
    m = TestClub(dist,day)
    counter += 1
    print str(counter)
    for i in range(len(Categories)):
        g = club(Categories[i], pdDistricts[i] , Days[i])
        if len(n) <= 5:


            n.append(g)

        else:
            for j in range(len(n)):
                if Sim(n[j],m) <= Sim(g,m):
                    n.remove(n[j])
                    if g not in n:

                        n.append(g)
                    break

    cate = MaxCat(n)
    for c in classes:
        if c == cate:
            sol.append(1)
        else:
            sol.append(0)
    fo.writerow(sol)

print "completed"





