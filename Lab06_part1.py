""" 
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
"""
class Team:
    
    def user_input():
        import datetime
        player_name = raw_input("Please Enter the name of Player :")
        match_date=raw_input("Type Date dd/mm/yy: ")
        d = datetime.datetime.strptime(match_date, "%d/%m/%y")
        player_score=int(raw_input("Please enter Player score:"))
        print player_name,d,  player_score
    user_input()


    
import datetime
player_stats=["rooney ",{datetime.date(2012,06,23),2}]
player_stats=['rooney ',{datetime.date(2012,06,25),3}]

player_stats=['ronaldo'][datetime.date(2012,06,19),0]
player_stats=['ronaldo'][datetime.date(2012,06,20),3]
player_stats=['torres '][datetime.date(2012,06,21),0]
player_stats=['torres '][datetime.date(2012,06,21),1]
"""

#player_stats["rooney"][,]
#print player_stats#, "\n", player_stats, "\n", player_stats, "\n", player_stats4, "\n", player_stats5, "\n", player_stats6

class Address:
    def __init__(self,number,street_address):
        self.number=number
        self.street_address=street_address
        Myadress=Address(2,'Malam')
print Address.Myadress

## implement highest_score

## implement highest_score_for_player



## implement highest_scorer











