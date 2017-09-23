def mix(colr1, colr2):
    if colr1 == colr2:
        return colr1
    elif colr1 == color(255,255,0) or colr2 == color(255,255,0):
        return color(255,255,0)
    elif colr1 == color(255):
        return colr2
    elif colr1 != colr2:
        return color(255,255,0)