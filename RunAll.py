import time


# Aho-Corasick algorithm for string matching: https://www.codespeedy.com/explain-the-aho-corasick-algorithm-for-pattern-searching-in-python/


class Ahomain:
    def __init__(self):
        self.go = {}
        self.out = []
        self.breaks = None


def aho_treeform(list1):
    main = Ahomain()

    for way in list1:
        point = main
        for sym in way:
            point = point.go.setdefault(sym, Ahomain())
        point.out.append(way)
    return main


def aho_state_transition(list1):
    main = aho_treeform(list1)
    queue = []
    for point in main.go.values():
        queue.append(point)
        point.breaks = main

    while len(queue) > 0:
        rightpoint = queue.pop(0)
        for clue, uniquepoint in rightpoint.go.items():
            queue.append(uniquepoint)
            firstpoint = rightpoint.breaks
            while firstpoint != None and not clue in firstpoint.go:
                firstpoint = firstpoint.breaks
            uniquepoint.breaks = firstpoint.go[clue] if firstpoint else main
            uniquepoint.out += uniquepoint.breaks.out

    return main


def aho_search(y, main, call):
    point = main
    for i in range(len(y)):
        while point != None and not y[i] in point.go:
            point = point.breaks
        if point == None:
            point = main
            continue
        point = point.go[y[i]]
        for design in point.out:
            call(i - len(design) + 1, design)


def found(loc, list1):
    #print("Pattern found at index %s" % (loc))
    pass


# Rabin Karp Code:
def search(pat, txt, q):
    starting_indexes = []
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
            j += 1
            if j == M:
                starting_indexes.append(str(i))
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0:
                t = t + q
    return starting_indexes


# Knutch Morris Pratt
# Python program for KMP Algorithm: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0
    computeLPSArray(pat, M, lps)
    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            #print("Pattern found at index " + str(i - j))
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    len = 0
    lps[0]
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


# Bad Character Heuristic Boyer Moore String Matching Algorithm

NO_OF_CHARS = 256


def badCharHeuristic(string, size):
    badChar = [-1] * NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


def BMsearch(txt, pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            #print("Pattern found at index = {}".format(s))
            s += m - badChar[ord(txt[s + m])] if s + m < n else 1
        else:
            s += max(1, j - badChar[ord(txt[s + j])])


# Boyer Moore Algorithm with Good Suffix heuristic


def preprocess_strong_suffix(shift, bpos, pat, m):
    i = m
    j = m + 1
    bpos[i] = j
    while i > 0:
        while j <= m and pat[i - 1] != pat[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j


def preprocess_case2(shift, bpos, pat, m):
    j = bpos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]


def BMGoodsearch(text, pat):
    s = 0
    m = len(pat)
    n = len(text)
    bpos = [0] * (m + 1)
    shift = [0] * (m + 1)
    preprocess_strong_suffix(shift, bpos, pat, m)
    preprocess_case2(shift, bpos, pat, m)
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == text[s + j]:
            j -= 1
        if j < 0:
            #print("Pattern found at index = %d" % s)
            s += shift[0]
        else:
            s += shift[j + 1]


# Brute force search
def brute_force_search(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1
        #if j == M:
            #print("Pattern found at index ", i)


def RunAllAlgorithms(file, pattern):
    Times = []
    f = open(file, "r")
    text = f.read()
    # Aho-Corasick algorithm
    #print("Initiating Aho-Corasick algorithm")
    start_time = time.time()
    list1 = [pattern]
    main = aho_state_transition(list1)
    aho_search(text, main, found)
    execution_time = time.time() - start_time
    #print(" time = ", execution_time)
    Times.append(execution_time)
    f.close()

    # Rabin-Karp algorithm
    #print("Initiating Rabin-Karp algorithm")
    starting_time = time.time()
    q = 101
    result = search(pattern, text, q)
    ending_time = time.time() - starting_time
    #print(result, " time = ", ending_time)
    #print(" time = ", ending_time)
    Times.append(ending_time)

    # Knutch Morris Pratt algorithm
    #print("Initiating Knutch Morris Pratt algorithm")
    start_time = time.time()
    KMPSearch(pattern, text)
    ending_time = time.time() - start_time
    #print(" time = ", ending_time)
    Times.append(ending_time)

    # Bayer Moore Bad Character heuristic algorithm
    #print("Initiating Bayer Moore Bad Character Heuristic algorithm")
    start_time = time.time()
    BMsearch(text, pattern)
    ending_time = time.time() - start_time
    #print(" time = ", ending_time)
    Times.append(ending_time)

    # Boyer Moore Good Suffix heuristic algorithm
    #print("Initiating Bayer Moore Good Suffix Heuristic algorithm")
    start_time = time.time()
    print(BMGoodsearch(text, pattern))
    ending_time = time.time() - start_time
    #print(" time = ", ending_time)
    Times.append(ending_time)

    # Brute Force Search
    #print("Initiating Brute Force Search algorithm")
    start_time = time.time()
    brute_force_search(pattern, text)
    ending_time = time.time() - start_time
    #print(" time = ", ending_time)
    Times.append(ending_time)
    return Times


def CalculateD(file):
    f = open(file, "r")
    text = f.read()
    List = []
    for i in text:
        if i not in file:
            List.append(i)
    return len(List)

########################################################


# Execute the code here
#file = "chimpanzee.txt"
#pattern = "GCATACGC"
#d = CalculateD(file)
#Times = RunAllAlgorithms(file, pattern)
    
#file2 = "Chimp_little_substrings.txt"
#pattern2 = "ABCDE"
#d2 = CalculateD(file2)
#Times2 = RunAllAlgorithms(file2, pattern2)

#for x in range(len(Times)):
    
    #difference = Times2[x] - Times[x]
    #average = (Times2[x] + Times[x]) / 2
    #dba = difference / average
    #percent = dba * 100
    #percent = round(percent, 2)
    #results.append(difference)
    #percentages.append(percent)
    
    #x = x + 1
       
#print("The difference between ", file, " and ", file2, " is ", "\nAho: ", \
      #results[0],  "    ", percentages[0],"%",  "\nRabin: ", results[1], "    ", percentages[1],"%", \
      #"\nKMP: ", results[2], "    ", percentages[2],"%", "\nBM bad: ", \
      #results[3], "    ", percentages[3],"%",  "\nBM good: ", results[4], "    ", percentages[4],"%", \
      #"\nBrute: ", results[5], "    ", percentages[5],"%")

###################################################################################

avg_chimp_times = [0,0,0,0,0,0]
avg_alt_times = [0,0,0,0,0,0]

                                        ###

#Execute the code here
file = "chimpanzee.txt"
#file = "abcde.txt"
pattern = "CA"
d = CalculateD(file)
for r in range(25):
    Times = RunAllAlgorithms(file, pattern)
    for z in range(6):
        avg_chimp_times[z] = avg_chimp_times[z] + Times[z]        
for s in range(6):
    avg_chimp_times[s] = avg_chimp_times[s] / 25
    
#print(avg_chimp_times)

# GCATACGC    
#avg_chimp_times = [1.8398387304941812, 2.66322478612264, 2.092763379414876, 1.3112665557861327, 1.4422272268931071, 1.535941260655721] 
   
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#avg_chimp_times = [1.6090520572662355, 2.557958345413208, 1.9065381145477296, 0.01679436683654785, 0.013165884017944336, 1.3151279067993165]
   
#file2 = "Chimp_little_substrings.txt"
#file2= "Chimp_not_found.txt"
#file2= "Chimp_random.txt"
#file2= "Chimp_spaces.txt"
#file2= "Chimp_special_chars.txt"
#file2= "Chimp_triple.txt"
#file2= "Chimp_A_then_Cs.txt"
#file2= "Chimp_bytes.txt"
#file2= "Chimp_c_and_g.txt"
file2= "Chimp_Cs_then_A.txt"
#file2= "Chimp_newlines.txt"
#file2 = "abcde.txt"
d = CalculateD(file2)
for w in range(25):
    Times2 = RunAllAlgorithms(file2, pattern)
    for q in range(6):
        avg_alt_times[q] = avg_alt_times[q] + Times2[q]        
for a in range(6):
    avg_alt_times[a] = avg_alt_times[a] / 25    
#print(avg_chimp_times, avg_alt_times)

results = []
percentages = []

for x in range(len(avg_chimp_times)):
    
    difference = avg_alt_times[x] - avg_chimp_times[x]
    average = (avg_alt_times[x] + avg_chimp_times[x]) / 2
    dba = difference / average
    percent = dba * 100
    percent = round(percent, 2)
    results.append(difference)
    percentages.append(percent)
    x = x + 1

print("The difference between chimpanzee.txt and ", file2, \
      "\nwhile searching for pattern ", pattern, \
      " \n and taking the average of 25 running times is ", \
      "\nAho: ", avg_chimp_times[0], "    ", results[0],  "    ", percentages[0],"%",  \
      "\nRabin: ", avg_chimp_times[0], "    ", results[1], "    ", percentages[1],"%", \
      "\nKMP: ", avg_chimp_times[0], "    ", results[2], "    ", percentages[2],"%", \
      "\nBM bad: ", avg_chimp_times[0], "    ", results[3], "    ", percentages[3],"%",  \
      "\nBM good: ", avg_chimp_times[0], "    ", results[4], "    ", percentages[4],"%", \
      "\nBrute: ", avg_chimp_times[0], "    ", results[5], "    ", percentages[5],"%")


############################################################################################################

#print(avg_chimp_times)



#one = [1.8555578994750976, 2.6661775875091553, 2.066421709060669, 1.3056711769104004, 1.46033917427063, 1.5539647483825683]
#two = [1.8202479553222657, 2.6655164527893067, 2.082110252380371, 1.3057082462310792, 1.4215178775787354, 1.5199720668792724]
#three = [1.8437103366851806, 2.657980318069458, 2.129758176803589, 1.3224202442169188, 1.444824628829956, 1.5338869667053223]

#for d in range(6):
    #avg_chimp_times[d] = (one[d] + two[d] + three[d]) / 3
    
#print(avg_chimp_times)

