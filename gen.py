# Wojciech Wolny
# 283786
# AAL Project under the supervision of Mgr Inż Kamila Deji
# Topic: "Podobieństwa cząstkowe ciągów"
# words generator file

import sys
import re
import random
import string


class Generate:

    def __init__(self, n=100, d=0.5, alphabet = 2):
        if not isinstance(n, int) or n <= 0:
            self.word_n = 100
        else:
            self.word_n = n
        if 0.0 <= d <= 1.0:
            self.word_d = d
        else:
            self.word_d = 0.5
        if alphabet > 0 and isinstance(alphabet, int):
            self.alphabet = alphabet
        else:
            self.alphabet = 2

    # generates word of length n
    # return a string of length {n}
    # d is a ratio of a's in a word
    def genWord(self, n=-1, d=-1.0, alphabet = -1):
        if n <= 0 or not isinstance(n, int):
            n = self.word_n
        if not 0.0 <= d <= 1.0:
            d = self.word_d
        if alphabet <= 0 or not isinstance(alphabet, int):
            alphabet = self.alphabet
        if alphabet == 1:
            return 'a'*n
        a_w = int(d * n)
        b_w = n - a_w
        b_letters = random.sample(string.ascii_letters[1:], min(alphabet-1, len(string.ascii_letters)-1))
        word = ''
        while a_w > 0 and b_w > 0:
            if random.randrange(n) < a_w:
                word += 'a'
                a_w -= 1
            else:
                word += random.choice(b_letters)
                b_w -= 1
            n -= 1
        if a_w > 0:
            for i in range(0, a_w):
                word += 'a'
        elif b_w > 0:
            for i in range(0, b_w):
                word += random.choice(b_letters)
        return word


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit("You should run: python gen.py -n<the length of the word> -d<ratio of a's in a word> -a<size of an alphabet>")

    if 2 <= len(sys.argv) <= 4:
        pattern = re.compile(r"^-n[0-9]+$")
        if pattern.match(sys.argv[1]):
            pat = re.compile(r"-n")
            strIn = pat.sub("", sys.argv[1])
            word_n = int(strIn)
        else:
            sys.exit("The number should be in this format: -n1000")
        pattern = re.compile(r"^-d(0(\.[0-9]*)?|1(\.0*)?)$")
        if len(sys.argv) >= 3 and pattern.match(sys.argv[2]):
            pat = re.compile(r"-d")
            strIn = pat.sub("", sys.argv[2])
            word_d = float(strIn)
            if word_d < 0.0 or word_d > 1.0:
                sys.exit("-d - the ratio should be between 0.0 and 1.0")
        else:
            word_d = 0.5
        pattern = re.compile(r"^-a[0-9]+$")
        if len(sys.argv) == 4 and pattern.match(sys.argv[3]):
            pat = re.compile(r"-a")
            strIn = pat.sub("", sys.argv[3])
            alphabet = int(strIn)
        else:
            alphabet = 2
    else:
        sys.exit("You should run: python gen.py -n<the length of the word> -d<ratio of a's in a word>  -a<size of an alphabet>")
    gen = Generate(word_n, word_d, alphabet)
    print(gen.genWord())
