from collections import defaultdict

g = defaultdict(str) | {(i,j): c for i,r in enumerate(open('input/4-4.txt'))
                                 for j,c in enumerate(r)}
G = list(g.keys())
D = (-1,0,1)

T = list("XMAS")
print(sum([g[i+di*n, j+dj*n] for n in range(4)] == T
       for di in D for dj in D for i,j in G))

T = list("MAS"), list("SAM")
print(sum([g[i+d,j+d] for d in D] in T
      and [g[i+d,j-d] for d in D] in T for i,j in G))