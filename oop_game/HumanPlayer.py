from Player import Player

ATTACK = 1

class HumanPlayer(Player):
    def act(self, field):
        print("> Choose action")
        print("1. Attack")  
        
        command = int( input() )

        if( command == ATTACK):
            print(">Choose a target team")
            teams = field.teams
            for i in range(len(teams)):
                team = teams[i]
                print(f"{i}.")
                team.info()
            
            chosen_team_index = int( input() )
            if( -1 < chosen_team_index and chosen_team_index < len(teams) ):
                print(">Choose a target enemy")
                chosen_team = teams[chosen_team_index]
                chosen_team_array = chosen_team.members
                for i in range(len(chosen_team_array)):
                    enemy = chosen_team_array[i]
                    print(f"{i}.")
                    enemy.info()
                
                chosen_enemy_index = int( input() )
                chosen_enemy = chosen_team_array[chosen_enemy_index]
                self.attack(chosen_enemy)