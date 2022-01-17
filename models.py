
class Player:
    def __init__(self,first_name = None,
                       last_name = None,
                       birthdate = None,
                          gender = None,  
                         ranking = None,
                           score = 0,
                       player_id = 0
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.player_id = player_id
    
    def __repr__(self):
        return self.first_name 

#Dans la classe Tournament la semaine dernière il n'y avait que self et self.players = []
class Tournament:
    def __init__(self, tournament_name = None,
                              location = None,
                       tournament_date = None,
                       number_of_tours = 4 ,
                          time_control = None,
                           description = None,
                                rounds = [],
                         tournament_id = None,
                ):

        self.players = []

        self.tournament_name = tournament_name
        self.location = location
        self.tournament_date = tournament_date
        self.time_control = time_control
        self.description = description
        self.tournament_id = tournament_id 
        
class Match:
    def __init__(self, player_1, player_2, result):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result = result
        
    
        