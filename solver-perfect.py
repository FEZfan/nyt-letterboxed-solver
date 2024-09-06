import string
import time
from letterboxedutils import *
from bitarray import bitarray, frozenbitarray

class Word:
    def __init__(self, word, chars, frozen = True):
        self.word = word
        self.bitarray = get_bitarray(word, chars, frozen)

def get_bitarray(word, chars, frozen = True):
    b = bitarray(12)
    if word == None: return b

    s = set(word)
    for i, c in enumerate(chars):
        b[i] = c in s
    return frozenbitarray(b) if frozen else bitarray(b)

def get_valid_words(words, sides, chars):
    to_remove = set()
    for w in words:
        if not validateWord(w,sides,chars): to_remove.add(w)
    return words - to_remove

def validateWord(word, sides, chars):
    letters = list(word)
    setletters = set(letters)
    if not setletters.issubset(chars): return False
    if not len(setletters) == len(letters): return False
    if len(setletters) == 1: return False

    i = 1
    while i < len(letters):
        if sides[letters[i]] == sides[letters[i-1]]: return False
        i += 1
    return True

def get_word_dict(words, chars):
    r = {}
    for i in string.ascii_uppercase:
        r[i] = {}
    for w in words:
        d = r[w[0]]
        w = Word(w[1:], chars)
        d[w.bitarray]=d.get(w.bitarray, frozenset()) | set([w])
    return r

def get_options(d, solution):
    r = set()
    b = solution.bitarray
    c = b.count(0)

    for k in d.keys():
        if (k & b) == bitarray(12):
            r |= d[k]

    return r

def solver(solution, depth, chars, validwords, words, maxdepth):
    if solution.bitarray.all():
        return solution

    if depth > maxdepth:
        return None

    last_char = solution.word[-1] if solution.word else None

    if last_char is None:
        for w in validwords:
            result = solver(Word(w, chars, frozen = False), depth + 1, chars, validwords, words, maxdepth)
            if result:
                return result
    else:
        if depth == maxdepth:
            options = words[last_char].get(frozenbitarray(~solution.bitarray), set())
        else:
            options = get_options(words[last_char], solution)

        for w2 in options:
            new_solution = Word(solution.word + ' - ' + last_char + w2.word, [])
            new_solution.bitarray = solution.bitarray | w2.bitarray
            result = solver(new_solution, depth + 1, chars, validwords, words, maxdepth)
            if result:
                return result

    return None

def main():
    print()
    
    f = input("wordlist: ")
    s = input("sides: ").upper()

    start = time.perf_counter()

    sides = get_sides(s)
    chars = get_chars(s)
    t = time.perf_counter()
    inputParsedTime = t-start

    wordlist = get_words(f)
    t2 = time.perf_counter()
    wordlistReadTime = t2-t

    validwords = get_valid_words(wordlist,sides,chars)
    t = time.perf_counter()
    wordlistPrunedTime = t-t2
    words = get_word_dict(validwords, chars)
    t2 = time.perf_counter()
    wordlistOrganisedTime = t2-t

    i = 0
    while i <= 12:
        i += 1
        s = solver(Word(None, chars), 0, chars, validwords, words, i)
        if s:
            t = time.perf_counter()
            totalTime = t - start
            algorithmTime = t - t2

            print('\n' + s.word)
            print()
            print(f"solution found in {round(totalTime, 3)}s")
            print("    parsing input        {0} ({1})".format(rndTime(inputParsedTime), timePortion(inputParsedTime,totalTime)))
            print("    reading wordlist     {0} ({1})".format(rndTime(wordlistReadTime), timePortion(wordlistReadTime,totalTime)))
            print("    pruning wordlist     {0} ({1})".format(rndTime(wordlistPrunedTime), timePortion(wordlistPrunedTime,totalTime)))
            print("    organising wordlist  {0} ({1})".format(rndTime(wordlistOrganisedTime), timePortion(wordlistOrganisedTime,totalTime)))
            print("    finding solution     {0} ({1})".format(rndTime(algorithmTime), timePortion(algorithmTime,totalTime)))
            return
    print("no perfect solutions")

if __name__ == '__main__':
    main()
