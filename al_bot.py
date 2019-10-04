#Al_bot

from re import *   # Loads the regular expression module.
import random
#max(stats.items(), key=operator.itemgetter(1))[0]
topic_dict = {'game':0, 'food': 0, 'dl': 0, 'computer': 0}
last_topic = {'topic':'none'}
PUNTS = ['Go on.',
         'Tell me about it more.',
         'Okay.',
         'What does that mean?',
         'Would you like to talk about food next?',
         'Would you like to talk about video games next?',
         'Would you like to talk about computer next?',
         'Would you like to talk about deep learning next?',
         'I enjoy talking to you.',
         'Cool!',
         'I am listening.',
         'That does not sound so good.',
         'That\'s right',
         'And then?',
         'What is that?',
         'How come?'
         ]


punt_count = 0 #define counters for remembering topics
def check_last(topic):
    return last_topic['topic'] == topic
def assign_last(topic):
    last_topic['topic'] = topic
def call_topics():
    topics = ['let\'s talk about food.',
          'let\'s talk about video games.',
          'let\'s talk about deep learning.',
          'let\'s talk about computers.']
    return random.choice(topics)
def reset_dic(key):
    topic_dict[key] = 2
    return
def sub_one_dic(key):
    topic_dict[key] -= 1
    return
def check_dic(key):
    return topic_dict[key]
def introduce():
    print('My name is Alan. My friends call me the Al.')
    print('Welcome to my gaming room!')
    print('What do you want to talk about?')
def al():#main function
    introduce()
    while True:
        the_input = input('TYPE HERE:>> ')
        if match('bye',the_input):
            print('Okay, nice talking to you.')
            return
        respond(the_input)

def respond(the_input):
    print(topic_dict)
    wordlist = split(' ',remove_punctuation(the_input))
    # undo any initial capitalization:
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0]=mapped_wordlist[0].capitalize()
    if 'game' in wordlist or 'games' in wordlist or topic_dict['game'] != 0:#rule 1 for game topic
        if check_last('game'):
            if 'fighting' in wordlist:
                print('I like fighting games, too.')
                return
            if 'like' in wordlist:
                print('I am crazy about that game, too!')
                return
            if 'favorite' in wordlist:
                print('My favorite game is Street Fighter')
                return
            if 'pc' in wordlist:
                print('I have built my own pc for gaming and deep learning')
                return
            if 'ps4' in wordlist:
                print('I use to have a ps4 but I sold it when I graduated from Indiana University.')
                return
            if 'xbox' in wordlist:
                print('I never own a xbox.')
                return
            print(rand_game())
            sub_one_dic('game')
            return
            

        else:
            if last_topic['topic'] == 'none':
                reset_dic('game')
                assign_last('game')
                print('What kind of video game do you like?')
                return               
            elif check_dic(last_topic['topic']) == 0:
                reset_dic('game')
                assign_last('game')
                print('What kind of video game do you like?')
                return
            else:
                pass
            
        


    if 'food' in wordlist or topic_dict['food'] != 0: #rule 2 for food topic
        print(topic_dict,wordlist)
        if check_last('food'):
            if 'like' in wordlist:
                print('I am crazy about it, too!')
                return
            if 'favorite' in wordlist:
                print('My favorite food is Mexican food')
                return
            if 'pizza' in wordlist:
                print('I love pizza.')
                return
            if 'chinese' in wordlist:
                print('I usually make my own Chinese food at home.')
                return
            if 'japanese' in wordlist:
                print('I like takoyaki.')
                return
            if 'burger' in wordlist:
                print('Burgers are the best.')
                return
            print(rand_food())
            sub_one_dic('food')
            return
        else:
            if last_topic['topic'] == 'none':
                reset_dic('food')
                assign_last('food')
                print('What kind of food do you like?')
                return
            elif check_dic(last_topic['topic']) == 0:
                reset_dic('food')
                assign_last('food')
                print('What kind of food do you like?')
                return
            else:
                pass
        return
    if 'deep' and 'learning' in wordlist or topic_dict['dl'] != 0: #rule 3 for deep learning topic
        print(topic_dict,wordlist)
        if check_last('dl'):
            if 'like' in wordlist:
                print('I like it, too!')
                return
            if 'favorite' in wordlist:
                print('My favorite model is GoogLeNet')
                return
            if 'rnn' in wordlist:
                print('RNNs are awesome, but with some minor problems.')
                return
            if 'data' in wordlist:
                print('I usually search dataset on Kaggle.')
                return
            if 'lstm' in wordlist:
                print('LSTM is awesome but hard to understand.')
                return
            if 'cnn' in wordlist:
                print('CNNs are good for image datasets.')
                return
            print(rand_dl())
            sub_one_dic('dl')
            return
        else:
            if last_topic['topic'] == 'none':
                reset_dic('dl')
                assign_last('dl')
                print('What kind of model do you like in deep learning?')
                return
            elif check_dic(last_topic['topic']) == 0:
                reset_dic('dl')
                assign_last('dl')
                print('What kind of model do you like in deep learning?')
                return
            else:
                pass
        return
    if 'computer' in wordlist or topic_dict['computer'] != 0: #rule 4 for computer topic
        print(topic_dict,wordlist)
        if check_last('computer'):
            if 'like' in wordlist:
                print('I love it.')
                return
            if 'laptop' in wordlist:
                print('I like MacOS more on laptops.')
                return
            if 'os' in wordlist:
                print('Windows is good but sometimes it upsets me.')
                return
            if 'gpu' in wordlist:
                print('I like good GPUs. They support both my games and work.')
                return
            if 'cpu' in wordlist:
                print('I think good CPUs are a little expensive. ')
                return
            if 'drive' in wordlist:
                print('Solid State Drive real impoves your PC')
                return
            print(rand_computer())
            sub_one_dic('computer')
            return
        else:
            if last_topic['topic'] == 'none':
                reset_dic('computer')
                assign_last('computer')
                print('What kind of conputer do you like?')
                return
            elif check_dic(last_topic['topic']) == 0:
                reset_dic('computer')
                assign_last('computer')
                print('What kind of conputer do you like?')
                return
            else:
                pass
        return
    if wordlist[0]=='':#rule 5 for empty input
        print(call_topics())
        return
    if wordlist[0:2] == ['i','am']:#rule 6 for 'I am...'
        print("Tell me why you are " +\
              stringify(mapped_wordlist[2:]) + '.')
        return
    if wpred(wordlist[0]): #rule 7 for questions
        print("You tell me " + wordlist[0] + ".")
        return
    if wordlist[0:2] == ['i','have']: # rule 8 for 'I have...'
        print("How long have you had " +\
              stringify(mapped_wordlist[2:]) + '.')
        return
    if dpred(wordlist[0]) and wordlist[1]==['i']: #rule 9 for sentence start with
        print('I\' not sure.')                    #[do, would ,should, can] followed by 'i'
        return
    if dpred(wordlist[0]) and wordlist[1]==['you']: #rule 10 for sentence start with
        print('I would rather not.')                #[do, would ,should, can] followed by 'you'
        return
    if wordlist[0:3] == ['i','feel','like']:#rule 11 for 'I feel like...'
        print("I feel the same way.")
        return
    if 'because' in wordlist:# rule 12 for 'because' in sentence
        print("I think you might be right.")
        return
    
    
    if wordlist[0:2] == ['you','are']: #rule 13 for 'you are...'
        print("You bet I am.")
        return
    if verbp(wordlist[0]): #rule 14 for a verb as the first word(exclude 'do')
        print(random.choice["Do you want me to " +\
              stringify(mapped_wordlist) + '?','Okay, I will do it.'])
        return
    if wordlist[0:3] == ['do','you','think']: #rule 15 'do you think...'
        print(random.choice(['Of course!', 'Sorry I can\'t agree with you on this one.']))
        return

    print(punt())
    
def rand_game(): # random reply when topic is game

    lst = ['I used to play a lot of video games with my friend at college.',
           'Video games are very productive right now.',
           'My favorite genre is fighting game, at least for now.',
           'I mostly play on PC.',
           'Tell me more about it.',
           'That is awesome.']
    return random.choice(lst)
def rand_food(): # random reply when topic is game

    lst = ['Food is the better thing you can get when you are upset.',
           'I love cooking.',
           'Sometimes I go out and eat Chinese food with friends',
           'I mostly eat at my apartment.',
           'Tell me more about it.',
           'That is awesome.']
    return random.choice(lst)
def rand_dl(): # random reply when topic is game

    lst = ['I have built a semantic video classifier with Tenserflow.',
           'You can do so many fun things with deep learning.',
           'I took a deep learning class last quarter.',
           'I run models on my own PC, but I am think about running them on cloud.',
           'Tell me more about it.',
           'That is awesome.']
    return random.choice(lst)
def rand_computer(): # random reply when topic is game

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

    return random.choice(PUNTS)

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
if __name__ == '__main__':
    al()# Launch the program.
