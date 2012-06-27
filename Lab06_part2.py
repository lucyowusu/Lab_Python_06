print 'Part II – Object-Oriented Programming I – Data Encapsulation'
print''

class Player:
    def __init__(self,firstname,lastname,team=None):
        self.firstname=firstname
        self.lastname=lastname
        self.scores=[]
        self.team=team
    def add_score(self,score):
        self.scores.append(score)
        
    def total_score(self):
        self.scores.sum(score)
        
        pass
    def average_score(self):
        pass
        
        
torres=Player('Fernando','Torres')

torres.add_score(0)
torres.add_score(0)
torres.add_score(1)
torres.add_score(0)
torres.add_score(1)

for i in torres.scores:
    print i
total_score=sum (add_score(score))
print torres.scores
        
