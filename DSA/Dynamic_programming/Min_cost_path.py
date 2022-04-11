'''                  DP matrix
[1, 2, 3],         [1          1+2= 3               3+3=6          ]
[4, 8, 2],  --->   [1+4= 5     min(1,3,5)+8= 9     min(3,6,9)+2=  5]
[1, 5, 3]          [5+1= 6     min(5,6,9)+5= 10    min(9,10,5)+3= 8]
                minimum cost required to reach from start to any box is
                particular value in dp matrix
                CODE IMPLEMENTATION:
                    first row and first column is cumulative sum
                    and remaining all blocks is
                        minimum of surrounding + original box value

        TIME COMPLEXITY--->O(m*n)
        SPACE COMPLEXITY-->O(1)
'''

def minCost(cost,row,col):
    # For 1st column
    for i in range(1,row):
        cost[i][0] += cost[i-1][0]

    # For 1st row
    for j in range(1,col):
        cost[0][j] += cost[0][j-1]

    # For rest of the 2d matrix
    for i in range(1,row):
        for j in range(1,col):
            cost[i][j] += (min(cost[i-1][j-1],min(cost[i-1][j],cost[i][j-1])))

    # Returning the value in
    # last cell
    return cost[row-1][col-1]

row = 3
col = 3
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCost(cost, row, col))

