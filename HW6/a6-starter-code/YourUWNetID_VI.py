'''YourUWNetID_VI.py
(rename this file using your own UWNetID.)

Value Iteration for Markov Decision Processes.
'''
from TowersOfHanoi import *
import random
# Edit the returned name to ensure you get credit for the assignment.
def student_name():
   return "Zhang, Tianyi" # For an autograder.

Vkplus1 = {}
Q_Values_Dict = {}

def one_step_of_VI(S, A, T, R, gamma, Vk):
   '''S is list of all the states defined for this MDP.
   A is a list of all the possible actions.
   T is a function representing the MDP's transition model.
   R is a function representing the MDP's reward function.
   gamma is the discount factor.
   The current value of each state s is accessible as Vk[s].
   '''

   '''Your code should fill the dictionaries Vkplus1 and Q_Values_dict
   with a new value for each state, and each q-state, and assign them
   to the state's and q-state's entries in the dictionaries, as in
       Vkplus1[s] = new_value
       Q_Values_Dict[(s, a)] = new_q_value

   Also determine delta_max, which we define to be the maximum
   amount that the absolute value of any state's value is changed
   during this iteration.
   '''
   
   global Q_Values_Dict, OPERATORS
   delta_lst = []
   #update Vi
   for i in range(len(S)):
      max_a = []
      for j in range(len(A)):
         sum_sp = 0
         for k in range(len(S)):
            t = T(S[i],A[j], S[k])
            if t > 0:
               r = R(S[i],A[j], S[k])
               s_sp = t*r+t*gamma*Vk[S[k]]
               sum_sp+=s_sp
         max_a.append(sum_sp)
      Vkplus1[S[i]] = max(max_a)
      delta_v = abs(Vkplus1[S[i]]-Vk[S[i]])
      delta_lst.append(delta_v)
   delta_max = max(delta_lst)
   #update Q
   for i in range(len(S)):
      for j in range(len(A)):
         sum_qsp = 0
         for k in range(len(S)):
            t = T(S[i],A[j], S[k])
            r = R(S[i],A[j], S[k])
            if t>0:
               qspap_lst = []
               for l in range(len(A)):
                  try:
                     q_spap = Q_Values_Dict[(S[k], A[l])]
                  except KeyError:
                     q_spap = 0
                  qspap_lst.append(q_spap)
               spap_max = max(qspap_lst)
               q_sp = t*r+t*gamma*spap_max
               sum_qsp+=q_sp
         Q_Values_Dict[(S[i], A[j])] = sum_qsp
         
               
                     
                  
               
   
   return (Vkplus1, delta_max)
   #return (Vk, 0) # placeholder

def return_Q_values(S, A):
   '''Return the dictionary whose keys are (state, action) tuples,
   and whose values are floats representing the Q values from the
   most recent call to one_step_of_VI. This is the normal case, and
   the values of S and A passed in here can be ignored.
   However, if no such call has been made yet, use S and A to
   create the answer dictionary, and use 0.0 for all the values.
   '''
   global Q_Values_Dict
   if not Q_Values_Dict:
      for i in range(len(S)):
         for j in range(len(A)):
            Q_Values_Dict[(S[i],A[j])] = 0.0
   
   return Q_Values_Dict # placeholder

Policy = {}
def extract_policy(S, A):
   '''Return a dictionary mapping states to actions. Obtain the policy
   using the q-values most recently computed.  If none have yet been
   computed, call return_Q_values to initialize q-values, and then
   extract a policy.  Ties between actions having the same (s, a) value
   can be broken arbitrarily.
   '''
   global Policy, Q_Values_Dict         
   Policy = {}
   # Add code here
   if not Q_Values_Dict:
      Q_Values_Dict = return_Q_values(S, A)
   for i in range(len(S)):
      max_lst = []
      for j in range(len(A)):
         q_v = Q_Values_Dict[(S[i],A[j])]
         max_lst.append(q_v)
      if max_lst:
         ind_lst = []
         for k in range(len(max_lst)):
            if max(max_lst) == max_lst[k]:
               ind_lst.append(k)
         if len(ind_lst) <= 1:
            Policy[S[i]] = A[ind_lst[0]]
         else:
            Policy[S[i]] = A[random.choice(ind_lst)]
            
         
            
   return Policy

def apply_policy(s):
   '''Return the action that your current best policy implies for state s.'''
   global Policy
   return Policy[s] # placeholder


