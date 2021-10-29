
import time


# d is the number of characters in the input alphabet
d = 4

# pat -> pattern
# txt -> text
# q -> A prime number


def search(pat, txt, q):
    
    starting_indexes = []
    
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    for i in range(M-1):
        h = (h*d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # check whether hash values of current window of text = hash value of pattern  
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break

            j += 1
            if j == M:
                #print ("Pattern found at index " + str(i))
                starting_indexes.append(str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q
                
    return starting_indexes

file = open('chimpanzee.txt', 'r')
txt = file.read()
pat = "GCATACGC"
q = 101  # A prime number

starting_time = time.time()

result = search(pat, txt, q)

ending_time = (time.time() - starting_time)

print(result, " time = ", ending_time)




# gotten from: https://cppsecrets.com/users/5629115104105118971091101011031055657495564103109971051084699111109/Python-Rabin-Karp.php




