#!/usr/bin/python3
'''MilestoneA.py
This runnable file will provide a representation of
answers to key questions about your project in CSE 415.

'''

# DO NOT EDIT THE BOILERPLATE PART OF THIS FILE HERE:

CATEGORIES=['Baroque Chess Agent','Wicked Problem Formulation and A* Search',\
  'Backgammon Agent that Learns','Hidden Markov Models: Algorithms and Applications']

class Partner():
  def __init__(self, lastname, firstname, uwnetid):
    self.uwnetid=uwnetid
    self.lastname=lastname
    self.firstname=firstname

  def __lt__(self, other):
    return (self.lastname+","+self.firstname).__lt__(other.lastname+","+other.firstname)

  def __str__(self):
    return self.lastname+", "+self.firstname+" ("+self.uwnetid+")"

class Who_and_what():
  def __init__(self, team, option, title, approach, workload_distribution, references):
    self.team=team
    self.option=option
    self.title=title
    self.approach = approach
    self.workload_distribution = workload_distribution
    self.references = references

  def report(self):
    rpt = 80*"#"+"\n"
    rpt += '''The Who and What for This Submission

Project in CSE 415, University of Washington, Autumn, 2019
Milestone A

Team: 
'''
    team_sorted = sorted(self.team)
    # Note that the partner whose name comes first alphabetically
    # must do the turn-in.
    # The other partner(s) should NOT turn anything in.
    rpt += "    "+ str(team_sorted[0])+" (the partner who must turn in all files in Catalyst)\n"
    for p in team_sorted[1:]:
      rpt += "    "+str(p) + " (partner who should NOT turn anything in)\n\n"

    rpt += "Option: "+str(self.option)+"\n\n"
    rpt += "Title: "+self.title + "\n\n"
    rpt += "Approach: "+self.approach + "\n\n"
    rpt += "Workload Distribution: "+self.workload_distribution+"\n\n"
    rpt += "References: \n"
    for i in range(len(self.references)):
      rpt += "  Ref. "+str(i+1)+": "+self.references[i] + "\n"

    rpt += "\n\nThe information here indicates that the following file will need\n"+\
     "to be submitted (in addition to code and possible data files):\n"
    rpt += "    "+\
     {'1':"Baroque_Chess_Agent_Report",'2':"Wicked_Problem_Forulation_Report",\
      '3':"Backgammon_Agent_That_Learns_Report", '4':"Hidden_Markov_Models_Report"}\
        [self.option]+".pdf\n"

    rpt += "\n"+80*"#"+"\n"
    return rpt

# END OF BOILERPLATE.

# Change the following to represent your own information:
tianyi = Partner("Tianyi", "Zhang", "zhang506")
mingyu = Partner("Mingyu", "Wang", "myw518")
team = [tianyi, mingyu]

OPTION = '2'
# Legal options are 1, 2, 4, and 4.

title = "A Formulated Solution for Seattle Crime Rate"

approach = '''Our approach will be to first understand the problem by identifying the properties
such as policies(actions), costs, state space, initial state and goal state. By researching
the real city policies that are designed to react to decreasing the crime rate,
we can estimate the cost of state transitions. Then we will formulate heuristic functions to measure the state distance.
Finally we will evaluate the heuristic functions by running an A* search in the given state space with starting state
and goal state.'''


workload_distribution = '''Mingyu will work on the definition and formulation of the problem.
Tianyi will work on defining the estimation of the cost, state space, starting state and goal state.
After all tasks above are done, both team members will work together coding and evaluation of
the A* search based on the given information.'''

reference1 = '''Wikipedia article on Wicked problem;
    URL: https://en.wikipedia.org/wiki/Wicked_problem (accessed Nov. 18, 2019)'''

reference2 = '''"6 proven policies for reducing crime and violence without gun control" by German Lopez,
    URL: https://www.vox.com/2016/2/15/10981274/crime-violence-policies-guns'''

our_submission = Who_and_what([tianyi, mingyu], OPTION, title, approach, workload_distribution, [reference1, reference2])

# You can run this file from the command line by typing:
# python3 who_and_what.py

# Running this file by itself should produce a report that seems correct to you.
if __name__ == '__main__':
  print(our_submission.report())