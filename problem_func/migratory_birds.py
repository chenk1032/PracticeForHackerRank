def migratory_birds(arr):
    d = {}
    for _ in set(arr):
        d[_] = arr.count(_)
    l = []
    for k, v in d.items():
        if v == max(list(d.values())):
            l.append(k)
    return min(l)


"""
Sample Input 1
11
1 2 3 4 5 4 3 2 1 3 4
Sample Output 1
3
"""
