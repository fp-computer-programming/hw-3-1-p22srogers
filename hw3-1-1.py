# Author: SMR (AMDG) 09/28/21
team_1_wins=input("How many wins did team one have? ")
team_1_ties=input("How many ties did team one have? ")
team_2_wins=input("How many wins did team two have? ")
team_2_ties=input("How many ties did team two have? ")
wins_1=int(3*team_1_wins)
ties_1=int(team_1_ties)
wins_2=int(3*team_2_wins)
ties_2=int(team_2_ties)
total_1= wins_1 + ties_1
total_2= wins_2+ties_2
if total_1 > total_2:
    print("Team One Won!")
else:
    print("Team Two Won!")
    
