#Al_bot
#topic in topic_dict are remembered by al bot for 2 rounds.
#general and food responses are cycle response
#other topics respond with random choice
#total of 15 rules marked
from re import *   # Loads the regular expression module.
import random #load random
topic_dict = {'game':0, 'food': 0, 'dl': 0, 'computer': 0} #topic count dict for memory
last_topic = {'topic':'none'} #last topic for memory
c_count_punts = [0] #count value for cycling
c_count_food = [0]
PUNTS = ['Hello.', #response for general(also cycle)
         'Okay.',
         'When can we do pokemon game.',
         'What does that mean?',
         'Would you like to talk about food next?',
         'Would you like to talk about video games next?',
         'Would you like to talk about computer next?',
         'Would you like to talk about deep learning next?',
         'I enjoy talking to you.',
         'When can we do pokemon game.',
         'That does not sound so good.',
         'That\'s right',
         ]
def agentName():
    return 'Al'
def check_last(topic): # check last topic == current or not
    return last_topic['topic'] == topic
def assign_last(topic): # assign current topic to last
    last_topic['topic'] = topic
def call_topics(): # call random topic sentence when '' input occurs
    topics = ['let\'s talk about food.',
          'let\'s talk about video games.',
          'let\'s talk about deep learning.',
          'let\'s talk about computers.']
    return random.choice(topics)
def reset_dic(key): # add count for memory(repeat this topic for n time)
    topic_dict[key] = 2
    return
def sub_one_dic(key):# count for topic -1
    topic_dict[key] -= 1
    return
def check_dic(key): # check topic count
    return topic_dict[key]
def introduce():# introduce al_bot
    out = 'My name is Alan. My friends call me the Al.\nWelcome to my gaming room!\nWhat do you want to talk about?'
    return out
    
def al():#main function
    print(introduce())
    while True:#give input line
        the_input = input('TYPE HERE:>> ')
        if match('bye',the_input):
            return 'Okay, nice talking to you.'
        respond(the_input)#call respond function

def respond(the_input):#function deal with text content
    wordlist = split(' ',remove_punctuation(the_input))
    # undo any initial capitalization:
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0]=mapped_wordlist[0].capitalize()
    #above are text process lines
    if 'game' in wordlist or 'games' in wordlist or topic_dict['game'] != 0:#rule 1 for game topic
        if check_last('game'):
            if 'fighting' in wordlist:
                return 'I like fighting games, too.'
            if 'like' in wordlist:
                return'I am crazy about that game, too!'
            if 'favorite' in wordlist:
                return'My favorite game is Street Fighter'
            if 'pc' in wordlist:
                return 'I have built my own pc for gaming and deep learning'
            if 'ps4' in wordlist:
                return'I use to have a ps4 but I sold it when I graduated from Indiana University.'
            if 'xbox' in wordlist:
                return'I never own a xbox.'
            
            if topic_dict['game']==0:
                reset_dic('game')
            else:
                sub_one_dic('game')
            return rand_game()
            

        else:
            if last_topic['topic'] == 'none':
                reset_dic('game')
                assign_last('game')
                return 'What kind of video game do you like?'              
            elif check_dic(last_topic['topic']) == 0:
                reset_dic('game')
                assign_last('game')
                return 'What kind of video game do you like?'
            else:
                pass
            
        


    if 'food' in wordlist or topic_dict['food'] != 0: #rule 2 for food topic
        if check_last('food'):
            if 'like' in wordlist:
                return 'I am crazy about it, too!'
            if 'favorite' in wordlist:
                return 'My favorite food is Mexican food'
            if 'pizza' in wordlist:
                return 'I love pizza.'
            if 'chinese' in wordlist:
                return 'I usually make my own Chinese food at home.'
            if 'japanese' in wordlist:
                return 'I like takoyaki.'
            if 'burger' in wordlist:
                return 'Burgers are the best.'
            
            if topic_dict['food']==0:
                reset_dic('food')
            else:
                sub_one_dic('food')
            return rand_food()
        else:
            if last_topic['topic'] == 'none':
                reset_dic('food')
                assign_last('food')
                return 'What kind of food do you like?'
            elif check_dic(last_topic['topic']) == 0:
                reset_dic('food')
                assign_last('food')
                return 'What kind of food do you like?'
            else:
                pass
        return
    if 'deep' and 'learning' in wordlist or topic_dict['dl'] != 0: #rule 3 for deep learning topic
        if check_last('dl'):
            if 'like' in wordlist:
                return random.choice(['I like it, too!','I don\'t like it'])
            if 'favorite' in wordlist:
                return 'My favorite model is GoogLeNet'
            if 'rnn' in wordlist:
                return 'RNNs are awesome, but with some minor problems.'
            if 'data' in wordlist:
                return 'I usually search dataset on Kaggle.'
            if 'lstm' in wordlist:
                return 'LSTM is awesome but hard to understand.'
            if 'cnn' in wordlist:
                return 'CNNs are good for image datasets.'
            if topic_dict['dl']==0:
                reset_dic('dl')
            else:
                sub_one_dic('dl')
            return rand_dl()
        else:
            if last_topic['topic'] == 'none':
                reset_dic('dl')
                assign_last('dl')
                return 'What kind of model do you like in deep learning?'
            elif check_dic(last_topic['topic']) == 0:
                reset_dic('dl')
                assign_last('dl')
                return 'What kind of model do you like in deep learning?'
            else:
                pass
        return
    if 'computer' in wordlist or topic_dict['computer'] != 0: #rule 4 for computer topic
        if check_last('computer'):
            if 'like' in wordlist:
                return 'I love it.'
            if 'laptop' in wordlist:
                return 'I like MacOS more on laptops.'
            if 'os' in wordlist:
                return 'Windows is good but sometimes it upsets me.'
            if 'gpu' in wordlist:
                return 'I like good GPUs. They support both my games and work.'
            if 'cpu' in wordlist:
                return 'I think good CPUs are a little expensive. '
            if 'drive' in wordlist:
                return 'Solid State Drive real improves your PC'
            if topic_dict['computer']==0:
                reset_dic('computer')
            else:
                sub_one_dic('computer')
            return rand_computer()
        else:
            if last_topic['topic'] == 'none':
                reset_dic('computer')
                assign_last('computer')
                return 'What kind of computer do you like?'
            elif check_dic(last_topic['topic']) == 0:
                reset_dic('computer')
                assign_last('computer')
                return 'What kind of computer do you like?'
            else:
                pass
        return
    if wordlist[0]=='':#rule 5 for empty input
        return call_topics()
    if wordlist[0:2] == ['i','am']:#rule 6 for 'I am...'
        out = "Why are you " +\
              stringify(mapped_wordlist[2:]) + '.'
        return out
    if wpred(wordlist[0]): #rule 7 for questions
        out = "You tell me " + wordlist[0] + "."
        return out
    if wordlist[0:2] == ['i','have']: # rule 8 for 'I have...'
        out = "It is interesting that you have " +\
              stringify(mapped_wordlist[2:]) + '.'
        return out
    if dpred(wordlist[0]) and wordlist[1]==['i']: #rule 9 for sentence start with
                          #[do, would ,should, can] followed by 'i'
        return 'I\'m not sure.'
    if dpred(wordlist[0]) and wordlist[1]==['you']: #rule 10 for sentence start with
            #[do, would ,should, can] followed by 'you'
        return 'I would rather not.'
    if wordlist[0:3] == ['i','feel','like']:#rule 11 for 'I feel like...'
        return "I feel the same way."
    if 'because' in wordlist:# rule 12 for 'because' in sentence
        return "I think you might be right."
    
    
    if wordlist[0:2] == ['you','are']: #rule 13 for 'you are...'
        return "You bet I am."
    if verbp(wordlist[0]): #rule 14 for a verb as the first word(exclude 'do')
        out = random.choice["Do you want me to " +\
              stringify(mapped_wordlist) + '?','Okay, I will do it.']
        return out
    if wordlist[0:3] == ['do','you','think']: #rule 15 'do you think...'
        out = random.choice(['Of course!', 'Sorry I can\'t agree with you on this one.'])
        return out

    return punt()
    
def rand_game(): # random reply when topic is game

    lst = ['I used to play a lot of video games with my friend at college.',
           'Video games are very productive right now.',
           'My favorite genre is fighting game, at least for now.',
           'I mostly play on PC.',
           'Tell me more about it.',
           'That is awesome.']
    return random.choice(lst)
def rand_food(): # cycle reply when topic is food

    lst = ['Food is the best thing you can get when you are upset.',
           'I love cooking.',
           'Sometimes I go out and eat Chinese food with friends',
           'I mostly eat at my apartment.',
           'Tell me more about it.',
           'That is awesome.']
    if c_count_food[0] == len(lst):
        c_count_food[0] = 1
    else:
        c_count_food[0] += 1
    return lst[c_count_food[0]-1]

def rand_dl(): # random reply when topic is deep learning

    lst = ['I have built a semantic video classifier with Tenserflow.',
           'You can do so many fun things with deep learning.',
           'I took a deep learning class last quarter.',
           'I run models on my own PC, but I am think about running them on cloud.',
           'Tell me more about it.',
           'That is awesome.']
    return random.choice(lst)
def rand_computer(): # random reply when topic is computer

    lst = ['I have built a PC by myself.',
           'You can do so many fun things PC.',
           'I like light-weighted laptops.',
           'I have always been a Windows user, but now I am think about move to Linux.',
           'Tell me more about it.',
           'That is awesome.']
    return random.choice(lst)
#util functions from shrink3
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
    return (w in ['do','can','should','would','could'])


def punt():
    'Returns one from a list of default responses.'
    if c_count_punts[0] == len(PUNTS):
        c_count_punts[0] = 1
    else:
        c_count_punts[0] += 1
    return PUNTS[c_count_punts[0]-1]



CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',#map dict
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
if __name__ == '__main__':
    al()# Launch the program.
