import parsetext
import traintext


#trained data is of the form [singles, doubles]

def ID(trained_data):
    input_sentence=input()
    words=parsetext.parse_unseen(input_sentence)
    data=[]
    


    #print(words)
