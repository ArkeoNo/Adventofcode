from collections import defaultdict

grid = defaultdict(str) | {(i,j): c for i,r in enumerate(open('input/4-4.txt'))
                                 for j,c in enumerate(r)}
grid_keys = list(grid.keys())
D = (-1,0,1)

T = list("XMAS")
print(sum([grid[i+di*n, j+dj*n] for n in range(4)] == T
       for di in D for dj in D for i,j in grid_keys))

T = list("MAS"), list("SAM")
print(sum([grid[i+d,j+d] for d in D] in T
      and [grid[i+d,j-d] for d in D] in T for i,j in grid_keys))


