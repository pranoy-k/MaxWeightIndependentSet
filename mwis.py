# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:33:25 2017

@author: Yonarp

Description: MaxWeight Independent Set of a Path Graph using Dynamic Programming
"""

path = "C:\\Users\Yonarp\OneDrive\Codes\MaxWeightIndependentSet\mwis1.txt"


with open(path) as file:
    numNodes = file.readline()
    print(numNodes)
    nodeWeights = list()
    for line in file:
        nodeWeights.append(int(line.strip()))

flagArray = [False]*len(nodeWeights)


def FindMWIS(nodeWeights):
    if (len(nodeWeights) == 1):
        return set(nodeWeights)
    if(flagArray[len(nodeWeights)-1]):
        return
    set1 = FindMWIS(list(nodeWeights[:-2]))
    set2 = FindMWIS(list(nodeWeights[:-1]))
    weight1 = nodeWeights[-1]+sum(set1)
    weight2 = sum(set2)

    if (weight1>weight2):
        return set1.add(nodeWeights[-1])
    else:
        return set2

#FindMWIS()