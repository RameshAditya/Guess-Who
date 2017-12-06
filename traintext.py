'''
Follow:{
            {word -
                {next word -
                                speaker
                                frequency
                }
            }
        }

'''

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

        if follow[tokens[i]][tokens[i+1]] not in follow.:
            follow[tokens[i]][tokens[i+1]]=[]

    #print(follow)
    
    #for i in range(len(tokens)-1):
        #If the given speaker has not been marked for the current next word
            
    return follow
