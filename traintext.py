'''
DATA FORMAT
doubles:{
            singles:{
                        {word -
                                {next word -
                                            [speaker
                                             frequency]
                                }
                        }
                    }
        }

singles:{
                        {word -
                                {next word -
                                            [speaker
                                             frequency]
                                }
                        }
                    }
'''

#temp value
tokens=['hello', 'my', 'name', 'is', 'aditya', 'and', 'this', 'is', 'a', 'sentence', 'and', 'part', 'of', 'a', 'test']

def train(singles, doubles, tokens, speaker):
    keys=[]
    for i in range(len(tokens)):
        keys.append(tokens[i])
    
    keys=list(set(keys))
    
    for i in range(len(keys)):
        temp={}
        if keys[i] not in doubles.keys():
            doubles[keys[i]]={}
            singles[keys[i]]=[]
        
    for i in range(len(tokens)-1):
        if tokens[i+1] not in list(doubles[tokens[i]]):
            doubles[tokens[i]][tokens[i+1]]=[]

    for i in range(len(tokens)-1):
        double_exists=0
        single_exists=0
        if len(list(doubles[tokens[i]][tokens[i+1]]))>0:
            for k in range(len(list(doubles[tokens[i]][tokens[i+1]]))):
                if doubles[tokens[i]][tokens[i+1]][k][0]==speaker:
                    doubles[tokens[i]][tokens[i+1]][k][1]+=1
                    double_exists=1
                    
        if len(list(singles[tokens[i]]))>0:
            for k in range(len(list(singles[tokens[i]]))):
                if singles[tokens[i]][k][0]==speaker:
                    singles[tokens[i]][k][1]+=1
                    single_exists=1

        if single_exists==0:
            singles[tokens[i]].append([speaker,1])
        
        if double_exists==0:
            doubles[tokens[i]][tokens[i+1]].append([speaker,1])

    return [singles, doubles]
