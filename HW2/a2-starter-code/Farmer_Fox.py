'''Farmer_Fox.py
by Tianyi Zhang
UWNetID: zhang506
Student number: 1868540

Assignment 2, in CSE 415, Autumn 2019.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''
#<METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Farmer and Fox"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['Tianyi. Zhang']
PROBLEM_CREATION_DATE = "10-OCT-2019"

# The following field is mainly for the human solver, via either the Text_SOLUZION_Client.
# or the SVG graphics client.

#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.

#<COMMON_CODE>
C=0  # array index to access chicken location
F=1# same idea for fox
G=2# same idea for grain
LEFT=0 # same idea for left side of river
RIGHT=1 # etc.

class State():

  def __init__(self, d=None):
    if d==None:
      d = {'items':[[1,0],[1,0],[1,0]], #each sublist represents the location of C,F,G (num 1 on index 0 means that the item on left side)
           'farmer':LEFT}
    self.d = d

  def __eq__(self,s2):
    for prop in ['items', 'farmer']:
      if self.d[prop] != s2.d[prop]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    p = self.d['items']
    txt = '[['+str(p[C][LEFT])+','+ str(p[F][LEFT])+','+str(p[G][LEFT])+'], ['+str(p[C][RIGHT])+','+str(p[F][RIGHT])+','+str(p[G][RIGHT])+']]'
    # txt = "\n Chicken on left:"+str(p[C][LEFT])+"\n"
    # txt += " Fox on left:"+str(p[F][LEFT])+"\n"
    # txt += " Grain on left:" + str(p[G][LEFT]) + "\n"
    # txt += " Chicken on right:"+str(p[C][RIGHT])+"\n"
    # txt += " Fox on right:"+str(p[F][RIGHT])+"\n"
    # txt += " Grain on right:" + str(p[G][RIGHT]) + "\n"
    side='left'
    if self.d['farmer']==1:
        side='right'
    txt += " farmer is on the "+side+"."
    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    news.d['items']=[self.d['items'][C_F_G][:] for C_F_G in [C,F,G]]
    news.d['farmer'] = self.d['farmer']
    return news

  def can_move(self,c,f,g):
      side = self.d['farmer']
      p = self.d['items']
      if c==1:# rule 1: chicken can move with farmer at anytime since fox and grain do not conflict
          if p[C][side] == 1:
              return True
      elif f==1: #rule 2: fox can only move with farmer when chicken and grain are not left behind(c and g conflict)
          if p[F][side] == 1:
              if p[C][side] == 1 and p[G][side] == 1:
                  return False
              else:
                  return True
      elif g == 1:
          if p[G][side] == 1:# rule 3: grain can only move with farmer when chicken and fox are not left behind(c and f conflict)
              if p[C][side] == 1 and p[F][side] == 1:
                  return False
              else:
                  return True
      else:
          if p[C][side] == 1 and p[G][side] == 1:
              return False
          elif p[C][side] == 1 and p[F][side] == 1:
              return False
          else:
              return True



  def move(self,c,f,g):
    '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the farmer carrying
     c,f,g.'''
    news = self.copy()      # start with a deep copy.
    side = self.d['farmer']         # location of farmer
    p = news.d['items']          # get the array of arrays of items.
    p[C][side] = p[C][side]-c     # Remove items from the current side.
    p[F][side] = p[F][side]-f
    p[G][side] = p[G][side]-g
    p[C][1-side] = p[C][1-side]+c # Add them at the other side.
    p[F][1-side] = p[F][1-side]+f
    p[G][1-side] = p[G][1-side]+g
    news.d['farmer'] = 1-side       # Move the farmer itself.
    return news

def goal_test(s):
  '''If all c,f,g are on the right, then s is a goal state.'''
  p = s.d['items']
  return (p[C][RIGHT]==1 and p[F][RIGHT]==1 and p[G][RIGHT]==1)

def goal_message(s):
  return "Congratulations on successfully bringing chicken, fox and grain across the river!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
CREATE_INITIAL_STATE = lambda : State(d={'items':[[1, 0], [1, 0],[1,0]], 'farmer':LEFT })
#</INITIAL_STATE>

#<OPERATORS>
MC_combinations = [(1,0,0),(0,1,0),(0,0,1),(0,0,0)]

OPERATORS = [Operator(
  "Cross the river with "+str(c)+" chicken and "+str(f)+" fox and "+str(g)+' grain.',
  lambda s, f1=f, c1=c,g1=g: s.can_move(c1,f1,g1),
  lambda s, f1=f, c1=c,g1=g: s.move(c1,f1,g1) )
  for (c,f,g) in MC_combinations]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>
