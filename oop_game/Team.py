class Team():
    def __init__(self, name, members = []):
        self.name = name
        self.members = members
        self.last_index = -1

    def addMember(self, member):
        self.members.append(member)

    def act(self, field):
        # 1. find who will play
        member = self.nextPlayer()
        
        # 2. make them play
        member.act(field)
    
    def nextPlayer(self):
        _len = len(self.members)
        for i in range(_len):
            next_index = (self.last_index + i + 1) % _len
            member = self.members[next_index]
            if( member.isAlive() ):
                self.last_index = next_index
                return member
        return None

    # check if there is a person alive 
    def isAlive(self):
        for member in self.members:
            if( member.isAlive() ):
                return True
        return False

    def isDead(self):
        return not self.isAlive()
    
    def isEmpty(self):
        return len(self.members) == 0

    def info(self):
        print(f"TEAM: {self.name}")
        for member in self.members:
            member.info()