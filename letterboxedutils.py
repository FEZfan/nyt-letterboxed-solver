def timePortion(t, total):
    return str(round(t/total*100, 2)) + '%'

def rndTime(t):
    return str(round(t, 3)).ljust(5,'0')+'s'

def get_sides(sides):
    sides = sides.split(',')
    r = {}
    for i,s in enumerate(sides):
        for c in set(s):
            r[c] = i
    return r

def get_chars(s):
    return set(s) - set([','])

def get_words(f):
    with open(f, 'r') as f:
        words = set([w.strip().upper() for w in f])
    return words