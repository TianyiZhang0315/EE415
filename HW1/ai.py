# dialog.py
# This program runs a dialog between two agents, which must be defined
# elsewhere as separate modules.

import al_bot as agentA
import a2 as agentB
import sys
#sys.stdout = open("/Users/tianyizhang/EE514/EE415/EE415/HW1/sampleConversation.txt", "w")
N_TURNS = 15

turn = 0
print(str(turn)+"A: "+agentA.agentName() + ': ' + agentA.introduce()+"\n")
print(str(turn)+"B: "+agentB.agentName() + ': ' + agentB.introduce()+"\n")
remark = "Good morning."
for i in range(N_TURNS):
    turn += 1
    remark = agentA.respond(remark)
    print(str(turn)+"A: "+agentA.agentName() + ': ' + remark+"\n")
    remark = agentB.respond(remark)
    print(str(turn)+"B: "+agentB.agentName() + ': ' + remark+"\n")