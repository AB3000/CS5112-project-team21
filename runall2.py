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
    pass

#########################################################

def RunAhoAlgorithm(file, pattern):

    f = open(file, "r")
    text = f.read()
    start_time = time.time()
    list1 = [pattern]
    main = aho_state_transition(list1)
    aho_search(text, main, found)
    execution_time = time.time() - start_time
    f.close()
    return execution_time

def CalculateD(file):
    f = open(file, "r")
    text = f.read()
    List = []
    for i in text:
        if i not in file:
            List.append(i)
    return len(List)

#######################################################

time1 = []
time2 = []

# if needed -- make sure to change the output print lines 
# from file or file2 variable to something concrete if you use this
f2 = open("Chimp_Cs.txt", "r")
Cpattern = f2.read()


repeats = 25

#Execute the code here
file = "Chimp_A_then_Cs.txt"
pattern = "AC"
file2 = "Chimp_A_then_Cs.txt"
pattern2 = "AC"
d = CalculateD(file)
for r in range(repeats):
    first_time = RunAhoAlgorithm(file, pattern)
    time1.append(first_time)
    second_time = RunAhoAlgorithm(file2, pattern2)
    time2.append(second_time)     

    

#file2 = "Chimp_little_substrings.txt"
#file2= "Chimp_not_found.txt"
#file2= "Chimp_random.txt"
#file2= "Chimp_spaces.txt"
#file2= "Chimp_special_chars.txt"
#file2= "Chimp_triple.txt"
#file2= "Chimp_A_then_Cs.txt"
#file2= "Chimp_bytes.txt"
#file2= "Chimp_c_and_g.txt"
#file2= "Chimp_Cs_then_A.txt"
#file2= "Chimp_newlines.txt"
#file2 = "abcde.txt"
#d = CalculateD(file2)

time1total = 0
time2total = 0

for s in range(repeats):
    time1total = time1total + time1[s]
    time2total = time2total + time2[s]
    print(time1[s], "     ", time2[s])
    
avg_time1 = time1total / repeats
avg_time2 = time2total / repeats

difference = avg_time2 - avg_time1
percent = (difference / avg_time1) * 100

if difference > 0:
    percent_moniker = "% increase"
else: 
    percent_moniker = "% decrease"

print("\n\n\n\n\n")
print("Difference between searching for ", pattern, " in ", file, " and ", pattern2, " in ", file2, "\n", \
      "average time1 = ", avg_time1, "   average time2 = ", avg_time2, "\n", \
      "average difference = ", difference, "  average percentage = ", round(percent,2), percent_moniker)




    