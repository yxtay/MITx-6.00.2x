import random

def sampleQuizzes():
    ntrials = 10000
    scores = []
    for i in xrange(ntrials):
        term1 = random.randrange(50, 81)
        term2 = random.randrange(60, 91)
        final = random.randrange(55, 96)
        scores.append(0.25 * term1 + 0.25 * term2 + 0.5 * final)
    count = sum([70 <= s and s <= 75 for s in scores])
    return count / float(ntrials)