#!/usr/bin/env python
# coding: utf-8

# In[1]:


def introduce():
    return('''My name is Pikachu, and I am a pokemon.
I was programmed by Mingyu Wang. If you don't like
the way I deal, contact him at myw518@uw.edu.
How can I help you?''')





def odd_even(x):
    if (x % 2) == 0:
        return 1
    else:
        return 0




from re import *   # Loads the regular expression module.
import random



def processing(the_input):
    
    wordlist = split(' ',remove_punctuation(the_input))
    # undo any initial capitalization:
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    
#1    
    if wpred(wordlist[0]):
        if input_history[the_input] == 1: 
            return[["You tell me",stringify(mapped_wordlist), "."],
         ["Let's talk about",stringify(mapped_wordlist), "."]][random.randint(0,1)]
        else:
            return [punt(),'You already mention that.']
        

 #2   
    if verbp(wordlist[0]):
        if input_history[the_input] == 1: 
            return["Why do you want me to " + stringify(mapped_wordlist) + '?']
        else:
            return [punt(),'You told that previous, but I want to the reason.']
 
 #3       
    if wordlist[0:2] == ['i','am'] or wordlist[0:2] == ['i','like']:
        if input_history[the_input] == 1: 
            return["Please tell me why you are " + stringify(mapped_wordlist[2:]) + '.']
        else:
            return [punt(),'I understand.']
        
#4        
    if wordlist[0:2] == ['i','have']:
        if input_history[the_input] == 1: 
            return["How long have you had " + stringify(mapped_wordlist[2:]) + '.']
        else:
            return [punt(),'I know. You already said it.']
    
#5       
    if wordlist[0:2] == ['you','are']:
        if input_history[the_input] == 1: 
            return["Oh yeah, I am " + stringify(mapped_wordlist[2:]) + '.']
        else:
            return [punt(),'I know.']
        
        
#6        
    if wordlist[0:2]==['can','you'] or wordlist[0:2]==['could','you']:
        if input_history[the_input] == 1: 
            return["Perhaps I " + wordlist[0] + ' ' + stringify(mapped_wordlist[2:]) + ', but let me ask my master first.']
        else:
            return [punt(),'After receiving the reply, I will contact you at once.']
            

#7    
    if wordlist[0]=='':
        if odd_even(input_history[the_input]) == 0: 
            return["Please say something."]
        else:
            return['I am hearing.']
#8        
    if wordlist[0:2] == ['i','feel']:
        if input_history[the_input] == 1: 
            return["I sometimes feel the same way."]
        else:
            return [punt(),'You said that feeling before.']
       
#9    
    if 'because' in wordlist:
        if input_history[the_input] == 1: 
            return["Is that really the reason?"]
        else:
            return[punt(),'You said that reason before.']
        
#10        
    if wordlist[0:3] == ['do','you','think']:
        if odd_even(input_history[the_input]) == 0: 
            return["Hmmm, This is beyond my ability. I don't know."]
        else:
            return["I think you should answer that yourself."]
#11        
    if 'no' in wordlist:
        if odd_even(input_history['no']) == 0: 
            return["Don't be so negative."]
        else:
            return['Why you so negative']
#12    
    if 'yes' in wordlist:
        if odd_even(input_history['yes']) == 0: 
            return["How can you be so sure?"]
        else:
            return['How can you be so certain?']
#13        
    if 'maybe' in wordlist:
        if odd_even(input_history['maybe']) == 0: 
            return["Be more decisive."]
        else:
            return['could you please make up you mind?']
    
#14        
    if 'you' in mapped_wordlist or 'You' in mapped_wordlist:
        if input_history[the_input] == 1:
            mapped_wordlist[0]=mapped_wordlist[0].capitalize()
            return [punt(),stringify(mapped_wordlist) + '?'] 
        else:
            return [punt(),'You already said it. Could you say something else?']
        
    
    
    return [punt()]

def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")    

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where','how','what'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do','can','should','would'])

PUNTS = ['Okey.',
         'Pika~',
         'I see.',]

punt_count = 0
def punt():
    'Returns one from a list of default responses.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 3]


CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])





CONTI = ['Please go on.',
         'Tell me more.',
         'what else would you like to talk to me?',
         "Let's move on."]

conti_count = 0
def conti():
    global conti_count
    conti_count += 1
    return CONTI[conti_count % 4]




def agentName():
    return 'Pikapi'





import random
input_history={'yes':0,'no':0,'maybe':0}

def respond(the_input):
    the_input = the_input.lower().strip()

    if match('bye',the_input):
        return('Goodbye!')

    words = [i.lower() for i in split(' ',remove_punctuation(the_input))]
    if 'yes' in words:
        input_history['yes'] += 1
    elif 'no'in words:
        input_history['no'] +=1
    elif 'maybe' in words:
        input_history['maybe'] +=1
    elif the_input not in input_history:
        input_history[the_input] = 1
    else:
        input_history[the_input] += 1
        
    ans = processing(the_input)
    if ans[0] in PUNTS:
        if len(input_history)-3 > 6:
    
            pot_input=[key for key in input_history if wpred(split(' ',remove_punctuation(key))[0])and key != the_input]

            if len(pot_input) >= 1:
                again_input = pot_input[random.randint(0,len(pot_input)-1)]
                input_history[again_input] = 1
                ans_2 = processing(again_input)
                ans.append(stringify(ans_2))
                return stringify(ans)
            else:
                ans.append(conti())
                return stringify(ans)
        else:
            ans
            return stringify(ans)
    else:
        return stringify(ans)
                        








