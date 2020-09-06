def sock_merchant(n, ar):
    p = 0
    for v in [ar.count(_) for _ in set(ar)]:
        if v >= 2: p += int(v / 2)
    return p
