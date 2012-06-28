# -*- coding: utf-8 -*-
#The Main Class
class Player:
    #Main Method
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team
#Method to Append Score
    def add_score(self,score):
        self.scores.append(score)
        print "Score :",
        print self.scores
#Method to Print Player and Score
    def print_score(self, score):
        print self.first_name,self.last_name
       
#Methode to calculate Total Score
    def total_score(self):
        total= sum (self.scores)
        print total
#Method to Calculate average Score
    def average_score(self):
        average=sum(self.scores)/number_of_scores
        print average
#Method Fernando Torres
#Creatint an instance of the Class        
tores=Player('Fernando', 'Torres')
print "Name of Player :",
tores.print_score(3)
n=0
nos=raw_input("Please Enter The number of scores:")
number_of_scores=float(nos)
#Looping to allow user to enter all scores
while n<number_of_scores:
    n+=1
    tores.add_score( float(raw_input("Please Enter Score for Fernando Torres:")))
    if n>=number_of_scores:
        break
#Printing Total Score
print "The Total Score for Fernando Torres is :",
tores.total_score()

#Printing Average Score
print "The Average Score for Fernando Torres is :",
tores.average_score()


class Team:
    portugal='portugal'
    spain='spain'    

    def __init__(self,name=None,player=None):#name,league,manager_name,points,Players=None):
        self.name=[]
##      self.player_league=league
##      self.player_manager=manager_name
##      self.player_points=points
        self.player=[]
    
#Method to Append Score
    def add_players(self,player1):
        self.player.append(player1)
        
        if player1=="RONALDO":
            print (self.player, "plays for Portugal")
        elif player1=="TORRES":
            print (self.player, "plays for Spain")
        else:
            print "This Player Belongs to no team"
    def __str__(self):
        newstr=self.spain+" "+self.portugal
        return newstr
        print newstr
##    def add_new_player(self,new_player):
##        self.name.append(new_player)
##        print self.name
       
        
        
my=Team()
my.add_players((raw_input("Please Enter the name for the player:").upper()))

class Match:
    def __init__(self,home,away,date,home_score,away_score):
        home_team=home
        away_team=away
        date=date# (an instance of the datetime.date class)
        home_scores=home_score#(dictionary with player_last_name : player_score key:value pairs )
        away_scores=away_score#(dictionary with player_last_name : player_score key:value pairs )


























