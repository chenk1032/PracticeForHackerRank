def bon_appetit(bill, k, b):
    c = int((sum(bill) - bill[k]) / 2)
    if c == b:
        return 'Bon Appetit'
    else:
        return str(b - c)
