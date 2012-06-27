class Player:
    
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores =[]
        self.team = team

    def add_score(self,date,score):
        self.scores.append(score)
    
    def total_score(self):
        return sum(self.scores)
    
    
    def average_score(self):
        return self.total_score()/float(len(self.scores))




torres = Player('Fernando','Torres')
scores = [0,0,1,0,1]
for eachscore in scores:
    torres.add_score('1-07-2012',eachscore)
print torres.average_score()


print 'Part iii'

class Team:
    def __init__(self,name,league,manager_name,points):       
        self.new_name=name
        self.new_league=league
        self.new_manager_name=manager_name
        self.new_points=points
        self.players=[]
    
    def add_player(self,player):
        self.players.append(player)
        return self.players

    def __str__(self):
        return  str(self.new_name)
    

portugal=Team('PORTUGAL','Series A','Mourinho',2)
spain=Team('SPAIN','Premiership','Ancelloti',1)


print spain

torres = Player('Fernando','Torres',spain)
ronaldo = Player('Ronaldo','Cristiano',portugal)

portugal.add_player(ronaldo)
spain.add_player(torres)





class Match():
    def __init__(self,home_team,away_team,date):
        self.new_home_team=home_team
        self.new_away_team=away_team
        self.new_date= date
        self.home_scores={}
        self.away_scores={}
        
    def home_score(self):
        s=0
        for each in self.home_scores:
            s=s+self.home_scores[each]
        return s    
        
        
    def away_score(self):
        s=0
        for each in self.away_scores:
            s=s+self.away_scores[each]
        return s   
        

    def winner(self):
        if self.home_score()>self.away_score():
            print 'Winner!  ',
            return self.new_home_team.new_name
        elif self.home_score()<self.away_score():
            print 'Winner!  ',
            return self.new_away_team.new_name
        else:
            return 'Draw'

    def add_score(self,player,scores):
        playerteam=player.team

        if playerteam==self.new_home_team:
            if player.last_name in self.home_scores:
                self.home_scores[player.last_name]+=scores
            else:
                self.home_scores[player.last_name]=scores
        if playerteam==self.new_away_team:
            if player.last_name in self.away_scores:
                self.away_scores[player.last_name]+=scores
            else:
                self.away_scores[player.last_name]=scores

print '*********************************************************'
euro_semi_final=Match(spain,portugal,'June 27th 2012')

euro_semi_final.add_score(torres,1)
euro_semi_final.add_score(ronaldo,5)
euro_semi_final.add_score(torres,1)
print euro_semi_final.winner()
                










