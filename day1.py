
with open('input/1-1.txt') as f:
    data = [list(map(int, line.split('   '))) for line in f.read().splitlines()]

list1, list2 = zip(*data)
list1, list2 = sorted(list1), sorted(list2)

distance = sum(abs(a - b) for a, b in zip(list1, list2))
print(distance)

similar = sum(n * list2.count(n) for n in list1)
print(similar)
    