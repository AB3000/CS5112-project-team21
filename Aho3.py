import time


# make a class AhoNode for each node on the trie (tree)
# helps for persistence, although is not necessary
class AhoNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None

# create the trie
def aho_create_forest(patterns):
    root = AhoNode()
    #print("root = ", root.goto, root.out, root.fail)

    # for each letter in patterns
    for path in patterns:
        node = root
        for symbol in path:                #symbol is each letter by letter in patterns
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root


def aho_create_statemachine(patterns):
    root = aho_create_forest(patterns)
    queue = []
    #for node in root.goto.itervalues():
    for node in root.goto.values():
        queue.append(node)
        node.fail = root

    while len(queue) > 0:
        rnode = queue.pop(0)

        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode != None and not key in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out

    return root


def aho_find_all(s, root, callback):
    node = root

    for i in range(len(s)):
        while node != None and not s[i] in node.goto:
            node = node.fail
        if node == None:
            node = root
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            callback(i - len(pattern) + 1, pattern)

############################
# Demonstration of work
def on_occurence(pos, patterns):
    #print("At pos %s found pattern: %s" % (pos, patterns))
    starting_index_of_pattern.append(pos)
    return starting_index_of_pattern
    

file = open('chimpanzee.txt', 'r')
text = file.read()
patterns = ['GCATACGC']
s = text

starting_index_of_pattern = []

start_time = time.time()

root = aho_create_statemachine(patterns)
aho_find_all(s, root, on_occurence)

execution_time = (time.time() - start_time)

print(starting_index_of_pattern, "  time to run: ", str(execution_time))

file.close()



# aho corasick gotten from: http://algo.pw/algo/64/python