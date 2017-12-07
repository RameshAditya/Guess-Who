'''
Follow:{
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

def train(follow, tokens, speaker):

    #follow={}
    keys=[]

    #Check for every individual word
    for i in range(len(tokens)):
        keys.append(tokens[i])

    '''
    for i in range(len(tokens)-1):
        keys.append((' '.join(tokens[i:i+2]),speaker))
    '''
    
    keys=list(set(keys))
    
    for i in range(len(keys)):
        temp={}
        if keys[i] not in follow.keys():
            follow[keys[i]]={}

    for i in range(len(tokens)-1):
        #CHECK IF THE GIVEN FOLLOWING WORD HAS ALREADY OCCURRED, IF YES THEN APPEND ELSE CREATE
        if tokens[i+1] not in list(follow[tokens[i]]):
            follow[tokens[i]][tokens[i+1]]=[]

    for i in range(len(tokens)-1):
        c=0
        if len(list(follow[tokens[i]][tokens[i+1]]))>0:
            for k in range(len(list(follow[tokens[i]][tokens[i+1]]))):
                if follow[tokens[i]][tokens[i+1]][k][0]==speaker:
                    follow[tokens[i]][tokens[i+1]][k][1]+=1
                    c=1
        if c==0:
            print('NEVER')
            follow[tokens[i]][tokens[i+1]].append([speaker,1])
        
    #for i in range(len(tokens)-1):
     #   follow[tokens[i]][tokens[i+1]]

    #print(follow)
    
    #for i in range(len(tokens)-1):
        #If the given speaker has not been marked for the current next word
            
    return follow
