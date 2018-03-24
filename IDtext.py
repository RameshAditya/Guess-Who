import matplotlib.pyplot as plt
import numpy as np
import parsetext
import traintext

data=[]
scores={}
#trained data is of the form [singles, doubles]
def ID(trained_data = [{}, {}]):
    global data
    print('Enter training data: ')
    input_sentence=input()
    print('Enter speaker name: ')
    speaker = input()
    #input_sentence += ' $'
    words=parsetext.parse_unseen(input_sentence)
    #print(words)
    data = traintext.train(trained_data[0], trained_data[1], words, speaker)
    print(data)
    print('Input more training data?')
    choice = input()
    if 'y' in choice.lower():
        ID(data)
x = 1
def show(word):
    global data,x
    graph_data = scores
    N = len(graph_data)
    frequencies = [scores[j] for j in scores.keys()]
    ind = np.arange(N)
    width = 0.35

    #fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x+=1
    rects1 = ax.bar(ind, frequencies, width, color='b', yerr=0)

    ax.set_ylabel('Frequencies')
    ax.set_title('Frequency per speaker')

    ax.set_xticks(ind + width/2)
    labels = ()
    for i in scores:
        labels+=(i,)
    ax.set_xticklabels(labels)
    plt.show()
    

#Only test on frequency of words
def test():
    global data, scores
    print('Enter unseen data: ')
    unseen_data = input()
    tokens = parsetext.parse_unseen(unseen_data)
    scores = {}
    for i in tokens:
        if i in data[0].keys():
            for j in range(len(data[0][i])):
                if data[0][i][j][0] not in scores.keys():
                    scores[data[0][i][j][0]]=data[0][i][j][1]
                else:
                    scores[data[0][i][j][0]]+=data[0][i][j][1]
        show(i)
    print(scores)
    
