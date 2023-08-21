# -*- coding: utf-8 -*-


import math

def Distance(Mode, *Co):
    k = len(Co)
    Results = {}
    for i in range(k):
        for j in range(i+1, k):
            if Mode == "Manhattan":
                distance = sum(abs(Co[i][l]-Co[j][l]) for l in range(len(Co[i])))
            elif Mode == "Euclidean":
                distance = math.sqrt(sum((Co[i][l]-Co[j][l])**2 for l in range(len(Co[i]))))
            Results[(Co[i], Co[j])] = distance
    return Results

print(Distance("Euclidean",(1.5,2),(2,1.5),(1.5,1.5)))