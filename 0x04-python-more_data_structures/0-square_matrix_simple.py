#!/usr/bin/python3

X = [[1,2,3],
    [ ,5,6],
    [7 ,8,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] * X[i][j]

for r in result:
   print(r)
