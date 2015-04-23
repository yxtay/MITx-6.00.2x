def probTest(limit):
    prob = 1 / 6.0
    throw = 1
    while prob > limit:
        prob *= 5 / 6.0
        throw += 1
    return throw