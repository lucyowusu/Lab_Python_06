"""
Lab_Python_06
Part 1
"""

import datetime

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/22/2012	| 1
"""

## create the player_stats data structure


player_stats={'rooney':[(datetime.date(2012,6,23),2),(datetime.date(2012,6,25),2)],\
              'ronaldo':[(datetime.date(2012,6,19),0),(datetime.date(2012,6,20),3)],\
              'torress':[(datetime.date(2012,6,19),0),(datetime.date(2012,6,20),0)]}
for i in player_stats:
    print i,player_stats[i]

## i chose the list in a data dictionary because the items in the dictionary are mutable.
print ''

print 'Question 2'
## implement highest_score
highest_score=

## implement highest_score_for_player



## implement highest_scorer





        

