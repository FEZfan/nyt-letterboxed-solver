import string
import time
from letterboxedutils import *

def get_valid_words(words, sides, chars):
    to_remove = set()
    for w in words:
        if not validateWord(w,sides,chars): to_remove.add(w)
    return words - to_remove

def validateWord(word, sides, chars):
    letters = list(word)
    if not set(letters).issubset(chars): return False

    i = 1
    while i < len(letters):
        if sides[letters[i]] == sides[letters[i-1]]: return False
        i += 1
    return True

def get_word_dict(words):
    r = {}
    for i in string.ascii_uppercase:
        r[i] = set()
    for w in words:
        r[w[0]].add(w)
    return r

def solver(current_word, depth, chars, validwords, words, maxdepth):
    if set(''.join(current_word)) == chars:
        return current_word

    if depth > maxdepth:
        return None

    last_char = current_word[-1] if current_word else None
    last_char = last_char[-1] if last_char else None

    if last_char is None:
        for w in validwords:
            result = solver([w], depth+1, chars, validwords, words, maxdepth)
            if result:
                return result
    else:
        for w2 in words.get(last_char, []):
            result = solver(current_word + [w2], depth+1, chars, validwords, words, maxdepth)
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
    words = get_word_dict(validwords)
    t2 = time.perf_counter()
    wordlistOrganisedTime = t2-t
    
    i = 0
    while i <= 12:
        i += 1
        s = solver([], 0, chars, validwords, words, i)
        if s:
            t2 = time.perf_counter()
            totalTime = t2 - start
            algorithmTime = t2 - t
            print('\n'+" - ".join(s))
            print()
            print(f"solution found in {round(totalTime, 3)}s")
            print("    parsing input        {0} ({1})".format(rndTime(inputParsedTime), timePortion(inputParsedTime,totalTime)))
            print("    reading wordlist     {0} ({1})".format(rndTime(wordlistReadTime), timePortion(wordlistReadTime,totalTime)))
            print("    pruning wordlist     {0} ({1})".format(rndTime(wordlistPrunedTime), timePortion(wordlistPrunedTime,totalTime)))
            print("    organising wordlist  {0} ({1})".format(rndTime(wordlistOrganisedTime), timePortion(wordlistOrganisedTime,totalTime)))
            print("    finding solution     {0} ({1})".format(rndTime(algorithmTime), timePortion(algorithmTime,totalTime)))
            return
    print("no solution")

if __name__ == '__main__':
    main()