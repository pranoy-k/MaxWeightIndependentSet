# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:58:36 2017

@author: Yonarp

MWIS without memoization and recursion
"""

path = "C:\\Users\Yonarp\OneDrive\Codes\MaxWeightIndependentSet\mwis1.txt"


with open(path) as file:
    numNodes = file.readline()
#    print(numNodes)
    nodeWeights = list()
    for line in file:
        nodeWeights.append(int(line.strip()))

MwIS = set()

A = [0]*len(nodeWeights)
A[1] = nodeWeights[0]
for i in range(2,len(nodeWeights)):
    if(A[i-1]>nodeWeights[i-1]+A[i-2]):
        A[i] = A[i-1]
    else:
        A[i] = nodeWeights[i-1]+A[i-2]

i=len(nodeWeights)-1
while(i>=0):
    if(A[i]>nodeWeights[i]+A[i-1]):
        i-=1
    else:
        MwIS.add(nodeWeights[i])
        i-=2

#print (MwIS)
#print (len(MwIS))
checkIndices =[1, 2, 3, 4, 17, 117, 517, 997]
checkVertices = [nodeWeights[i-1] for i in checkIndices]

f = lambda x: (x in MwIS)
result = map(f,checkVertices)
print (list(result))