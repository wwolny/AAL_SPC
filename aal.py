# Wojciech Wolny
# 283786
# AAL Project under the supervision of Mgr Inż Kamila Deji
# Topic: "Podobieństwa cząstkowe ciągów"
# main file

import sys
import re
import time
from gen import Generate


class PrefixSum:

    def __init__(self, m, filename="", n=0, d=0.0, k=0, step=0, r=0, a=2):
        self.mode = m
        self.filename = filename
        self.word_n = n
        self.word_d = d
        self.word_k = k
        self.word_step = step
        self.word_r = r
        self.current_word = ""
        self.word_a = a

    # give to the output sum of longest common prefix with the word for suffixes of the word
    def print_result(self, lines=None):
        if lines is None:
            lines = []
        for i in range(0, len(lines)):
            print(self.pref_pref(lines[i]))

    # give to the output table with information about
    # coefficients of accordance of theoretical complexity and time measurement
    def print_table(self, t_n=None):
        if t_n is None:
            t_n = []
        print("|###Algorytm z asymptotą O(T(n))###|")
        print("|==================================|")
        print("|n      |t(n)[ms]       |q(n)      |")
        print("|==================================|")
        if self.word_k != len(t_n):
            print("Error occured")
        else:
            c = t_n[(int(self.word_k / 2))] / (self.word_n + self.word_step * (self.word_k / 2))
            for i in range(0, self.word_k):
                q_n = round(t_n[i] / (c * (self.word_n + self.word_step * i)), 2)
                print("|" + str(self.word_n + self.word_step * i) + " " * (
                        7 - len(str(self.word_n + self.word_step * i))) + ""
                                                                          "|" + str(round(t_n[i], 2)) + " " * (
                              15 - len(str(round(t_n[i], 2)))) + ""
                                                                 "|" + str(q_n) + " " * (10 - len(str(q_n))) + "|")
        print("|==================================|")

    # print comparison for O(N^2) algorithm and O(N) algorithm
    def print_csv(self, t_n_N2=None, t_n_N=None, sum_N2=None, sum_N=None):
        if sum_N is None:
            sum_N = []
        if sum_N2 is None:
            sum_N2 = []
        if t_n_N is None:
            t_n_N = []
        if t_n_N2 is None:
            t_n_N2 = []
        print("n,N^2:t(n)[ms],N^2:q(n),N^2:sum,N:t(n)[ms],N:q(n),N:sum")
        c_N2 = t_n_N2[(int(self.word_k / 2))] / ((self.word_n + self.word_step * (self.word_k / 2)) ** 2)
        c_N = t_n_N[(int(self.word_k / 2))] / (self.word_n + self.word_step * (self.word_k / 2))
        for i in range(0, self.word_k):
            q_n_N2 = round(t_n_N2[i] / (c_N2 * (self.word_n + self.word_step * i) ** 2), 2)
            q_n_N = round(t_n_N[i] / (c_N * (self.word_n + self.word_step * i)), 2)
            print(
                str(self.word_n + self.word_step * i) + "," + str(round(t_n_N2[i], 2)) + "," + str(q_n_N2) + "," + str(
                    sum_N2[i]) + "," + str(round(t_n_N[i], 2)) + "," + str(q_n_N) + "," + str(sum_N[i]))

    # ## Algorithm #1 ## #
    # O(n*n/2)
    # counts number of the exact same values
    # for the strings x and y from the beginning
    @staticmethod
    def count_str(x='', y=''):
        if x == '' or y == '':
            return 0
        count = 0
        if len(x) > len(y):
            for i in range(0, len(y)):
                if x[i] == y[i]:
                    count += 1
                else:
                    break
        else:
            for i in range(0, len(x)):
                if x[i] == y[i]:
                    count += 1
                else:
                    break
        return count

    # algorithm to count the similarity of main strong and it's suffixes
    def brute_force(self, x=''):
        count = 0
        for i in range(0, len(x)):
            count += self.count_str(x, x[i:])
        return count

    # ## END of Algorithm #1 ## #

    # ## Algorithm #2 ## #
    # O(n)
    def slow_scan(self, j, k):
        n = len(self.current_word)
        k = max(k, j)
        i = k - j
        while k < n and self.current_word[i] == self.current_word[k]:
            i += 1
            k += 1
        return k - j

    def pref_pref(self, x=''):
        n = len(x)
        # length of the longest common string starting at j position and the string
        PREF = [0] * (n)
        res = n
        s = 0
        PREF[0] = 0
        self.current_word = x
        # calculates value for suffix starting at j position
        for j in range(1, n):
            # if we have updated s in previous iteration k is going to be 1, if we used assigning values
            # it is 1 bigger then previous k
            # we use k for checking for the length of the period in which we can rewrite value
            k = j - s
            # if PREF[s] is big and PREF[k] is small
            # we can rewrite value from PREF[k]
            if k + PREF[k] < PREF[s]:
                PREF[j] = PREF[k]
            # else check following values for position j nad update s
            else:
                PREF[j] = self.slow_scan(j, s + PREF[s])
                s = j
            res += PREF[j]
        return res

    # ## END of Algorithm #2 ## #

    def run(self):
        if self.mode == 1:
            file = open(self.filename, 'r')
            lines = []
            for line in file:
                lines.append(line.strip())
            file.close()
            self.print_result(lines)
        elif self.mode == 2:
            gen = Generate(self.word_n, self.word_d, self.word_a)
            word = gen.genWord()
            score = self.pref_pref(word)
            print(word + "," + str(score))
        elif self.mode == 3:
            n_arr = []
            gen = Generate(self.word_n, self.word_d, self.word_a)
            for k in range(0, self.word_k):
                lines = []
                t_instance = []
                for r in range(0, self.word_r):
                    # Generate words with different ratio of a's in a word
                    lines.append(gen.genWord(self.word_n + k * self.word_step, r / self.word_r, self.word_a))
                    start = time.time()
                    self.pref_pref(lines[r])
                    end = time.time()
                    # The time should be in ms not seconds
                    t_instance.append((end - start) * 1000)
                n_arr.append(sum(t_instance) / self.word_r)
            self.print_table(n_arr)
        elif self.mode == 4:
            n_arrN2 = []
            n_arrN = []
            sum_N2 = []
            sum_N = []
            gen = Generate(self.word_n, self.word_d)
            for k in range(0, self.word_k):
                lines = []
                t_instanceN2 = []
                t_instanceN = []
                result_N = 0
                result_N2 = 0
                for r in range(0, self.word_r):
                    # Generate words with different ratio of a's in a word
                    lines.append(gen.genWord(self.word_n + k * self.word_step, r / self.word_r))
                    start = time.time()
                    result_N2 += self.brute_force(lines[r])
                    end = time.time()
                    startN = time.time()
                    result_N += self.pref_pref(lines[r])
                    endN = time.time()
                    # The time should be in ms not seconds
                    t_instanceN2.append((end - start) * 1000)
                    t_instanceN.append((endN - startN) * 1000)
                sum_N2.append(result_N2)
                sum_N.append(result_N)
                n_arrN.append(sum(t_instanceN) / self.word_r)
                n_arrN2.append(sum(t_instanceN2) / self.word_r)
            self.print_csv(n_arrN2, n_arrN, sum_N2, sum_N)


class ReadTerminal:
    def __init__(self, argv):
        self.argv = argv

    def read_mode(self, arg):
        if arg == "-m1":
            return 1
        elif arg == "-m2":
            return 2
        elif arg == "-m3":
            return 3
        elif arg == "-m4":
            return 4
        else:
            return 0

    def read_filename(self, arg):
        pattern = re.compile(r"^.*\.txt$")
        if pattern.match(arg):
            return arg
        else:
            return ""

    def read_n(self, arg):
        pattern = re.compile(r"^-n[0-9]+$")
        if pattern.match(arg):
            pat = re.compile("-n")
            strIn = pat.sub("", arg)
            return int(strIn)
        else:
            return 0

    def read_k(self, arg):
        pattern = re.compile(r"^-k[0-9]+$")
        if pattern.match(arg):
            pat = re.compile("-k")
            strIn = pat.sub("", arg)
            return int(strIn)
        else:
            return 0

    def read_step(self, arg):
        pattern = re.compile(r"^-step[0-9]+$")
        if pattern.match(arg):
            pat = re.compile("-step")
            strIn = pat.sub("", arg)
            return int(strIn)
        else:
            return 0

    def read_r(self, arg):
        pattern = re.compile(r"^-r[0-9]+$")
        if pattern.match(arg):
            pat = re.compile("-r")
            strIn = pat.sub("", arg)
            return int(strIn)
        else:
            return 0

    def read_d(self, arg):
        pattern = re.compile(r"^-d(0(\.[0-9]*)?|1(\.0*)?)$")
        if pattern.match(arg):
            pat = re.compile("-d")
            strIn = pat.sub("", arg)
            return float(strIn)
        else:
            return -1

    def read_a(self, arg):
        pattern = re.compile(r"^-a[0-9]+$")
        if pattern.match(arg):
            pat = re.compile("-a")
            strIn = pat.sub("", arg)
            return int(strIn)
        else:
            return -1

    def read_terminal(self):
        error = ""
        word_n = 0
        filename = ""
        word_d = 0.0
        word_k = 0
        word_step = 0
        word_r = 0
        word_a = 2
        if len(self.argv) < 2:
            error = "Not enough arguments. Read readme.txt to find out how to use this program."
        else:
            mode = self.read_mode(self.argv[1])
            if mode == 0:
                error = "Read readme.txt to find out how to use this program."
            elif mode == 1:
                if len(self.argv) == 3:
                    filename = self.read_filename(self.argv[2])
                    if filename == "":
                        error = "The file should end with .txt extension"
                else:
                    error = "You should run: python aal.py -m1 <name of the file>.txt"
            elif mode == 2:
                if 3 <= len(self.argv) <= 5:
                    word_n = self.read_n(self.argv[2])
                    if word_n == 0:
                        error = "The number should be in this format: -n1000"
                    if len(sys.argv) >= 4:
                        word_d = self.read_d(self.argv[3])
                        if word_d == -1:
                            error = "-d - the ratio should be between 0.0 and 1.0"
                    else:
                        word_d = 0.5
                    if len(sys.argv) == 5:
                        word_a = self.read_a(self.argv[4])
                        if word_a == -1:
                            error = "The number should be in this format: -a2"
                else:
                    error = "You should run: python aal.py -m2 -n<the length of the longest word in generated file> " \
                            "-d<ratio of a's in a word> -a<size of an alphabet>"
            elif mode == 3 or mode == 4:
                if 6 <= len(sys.argv) <= 7:
                    word_n = self.read_n(self.argv[2])
                    if word_n == 0:
                        error = "The number should be in this format: -n1000"
                    word_k = self.read_k(self.argv[3])
                    if word_k == 0:
                        error = "The number should be in this format: -k30"
                    word_step = self.read_step(self.argv[4])
                    if word_step == 0:
                        error = "The number should be in this format: -step500"
                    word_r = self.read_r(self.argv[5])
                    if word_r == 0:
                        error = "The number should be in this format: -r15"
                    if len(sys.argv) == 7:
                        word_a = self.read_a(self.argv[6])
                        if word_a == -1:
                            error = "The number should be in this format: -a2"
                elif mode == 3:
                    error = "You should run python aal.py -m3 -n<the length of the shortest word in generated file> " \
                            "-k<number of problems> -step<number of steps> -r<how many instances of a problem> -a<size of " \
                            "an alphabet>"
                else:
                    error = "You should run python aal.py -m4 -n<the length of the shortest word in generated file> " \
                            "-k<number of problems> -step<number of steps> -r<how many instances of a problem> -a<size " \
                            "of an alphabet>"
            if len(error) > 0:
                return error
            return [mode, filename, word_n, word_d, word_k, word_step, word_r, word_a]
        return error


# main function: reads arguments from terminal and runs program
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Not enough arguments. Read readme.txt to find out how to use this program.")
    user = ReadTerminal(sys.argv)
    mode = user.read_terminal()
    if isinstance(mode, str):
        print(mode)
    else:
        prefix_sum = PrefixSum(mode[0], mode[1], mode[2], mode[3], mode[4], mode[5], mode[6])
        prefix_sum.run()

