# 2차원 리스트 test

grid = [[x for x in range(5)] for i in range(5)]
print(*grid, sep='\n')
result = []

col, row = 2, 2

for i in range(len(grid) - col + 1):
    for j in range(len(grid[0]) - row + 1):
        total = 0
        for x in range(row):
            for y in range(col):
                total += grid[x+j][y+i]
        
        result.append(total)
    
print(result)