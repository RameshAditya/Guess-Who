'''
Components of Project are -
Parser - returns text parsed and cleaned
builder - builds a n-gram markov model
predicter - has the scoring function and makes the educated guesses
__init__ - main driver program
'''

def parse_unseen(s):
    allow='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #add full stop in remove?
    remove='!@#$%^&*()_\'-+=[{]}\||;:",<>/?/'

    #Read in to string here via file handling or twitter later
    #s='Hello, my name is Aditya, and this is a sentence! (and part of a test case...)'
    #s='D18: Practiced the implementation of the KMP algorithm, spent time on dynamic programming algorithms, brushed up on Kruskal\'s MST algorithm and posted an article explaining Moore\'s voting algorithm. Read the basics of finding the LCA between two nodes in a tree. #100DaysOfCode'
    #s='D17: Read up on the KMP linear time string matching algorithm. Learnt Moore\'s voting algorithm. Wrote another blog post. Finished up the previous post on union-find. Revised C++ STL. And now working on graph theory. Continued coursera\'s #MachineLearning course. #100DaysOfCode'

    buf=''
    words=[]
    for i in range(len(s)):
        if s[i] in allow:
            buf+=s[i].lower()
        if s[i]==' ':
            words.append(buf)
            buf=''
        if s[i] in remove:
            continue
    words.append(buf)
    return words

def parse_cumulative(tokens):
    allow='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #add full stop in remove?
    remove='!@#$%^&*()_\'-+=[{]}\||;:",<>/?/'

    #Read in to string here via file handling or twitter later
    s='Hello, my name is Aditya, and this is a sentence! (and part of a test case...)'
    #s='D18: Practiced the implementation of the KMP algorithm, spent time on dynamic programming algorithms, brushed up on Kruskal\'s MST algorithm and posted an article explaining Moore\'s voting algorithm. Read the basics of finding the LCA between two nodes in a tree. #100DaysOfCode'
    #s='D17: Read up on the KMP linear time string matching algorithm. Learnt Moore\'s voting algorithm. Wrote another blog post. Finished up the previous post on union-find. Revised C++ STL. And now working on graph theory. Continued coursera\'s #MachineLearning course. #100DaysOfCode'

    buf=''

    for i in range(len(s)):
        if s[i] in allow:
            buf+=s[i].lower()
        if s[i]==' ':
            tokens.append(buf)
            buf=''
        if s[i] in remove:
            continue
    tokens.append(buf)
    return tokens
