import time

class Field():
    def __init__(self, team_a, team_b):
        self.teams = [team_a, team_b]
        self.fightFinished = False
        self.turn = 0

    def startFight(self, sleeptime = 0):
        self.turn = 0
        while( not self.fightFinished ):
            team_index = self.turn % len(self.teams)
            team = self.teams[ team_index ]

            if( team.isAlive() ):
                team.act(self)

            self.checkStatus()
            self.info()
            self.turn = self.turn + 1
        
            time.sleep(sleeptime)

    def checkStatus(self):
        alive_count = 0
        for i in range(len(self.teams)):
            team = self.teams[i]
            if( team.isAlive() ):
                alive_count += 1
        
        self.fightFinished = alive_count == 1


    def info(self):
        print(f"TURN : {self.turn}")
        for team in self.teams:
            team.info()