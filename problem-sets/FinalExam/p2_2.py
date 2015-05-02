def mean(x):
    return sum(x) / len(x)
    
def stdDev(x, mu = None):
    sse = 0
    if not mu:
        mu = mean(x)
    for el in x:
        sse += (el - mu) ** 2
    var = float(sse) / (len(x))
    return var ** 0.5
    
a = [0,1,2,3,4,5,6,7,8]
b = [5,10,10,10,15]
c = [0,1,2,4,6,8]
d = [6,7,11,12,13,15]
e = [9,0,0,3,3,3,6,6]

for x in [a, b, c, d, e]:
    print "%.2f, %.2f" % (mean(x), stdDev(x))
    
def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)
    
for x in [a, b, c, d, e]:
    print '%.2f' % possible_variance(x)