import random

class Player:
    def __init__(self, name, batting, bowling, fielding, running, experience):
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.running = running
        self.experience = experience

    def __str__(self):
        return self.name

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []
        self.total_score = 0

    def select_captain(self, player):
        self.captain = player

    def send_next_batsman(self):
        if len(self.batting_order) > 0:
            return self.batting_order.pop(0)
        else:
            return None

    def choose_bowler(self):
        return random.choice(self.players)

    def decide_batting_order(self):
        random.shuffle(self.players)
        self.batting_order = self.players[:]

    def update_score(self, runs):
        self.total_score += runs

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

    def calculate_probability(self, player):
        return (
            player.batting * self.fan_ratio +
            player.bowling * self.pitch_conditions +
            player.fielding * self.home_advantage +
            player.running * self.size +
            player.experience
        )

class Umpire:
    def __init__(self):
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def predict_outcome(self, bowler, batsman):
        bowler_probability = bowler.bowling
        batsman_probability = batsman.batting
        total_probability = bowler_probability + batsman_probability
        bowler_probability /= total_probability
        batsman_probability /= total_probability
        outcome = random.choices(["out", "not_out"], [bowler_probability, batsman_probability])[0]
        if outcome == "out":
            self.wickets += 1
        return outcome

    def make_decision(self, bowler):
        decision = None

        # Implement logic to make decisions based on the match situation
        if bowler.bowling < 0.3:
            decision = "no_ball"
        elif bowler.bowling > 0.9:
            decision = "wide_ball"
        else:
            decision = "normal"

        return decision

class Commentator:
    def __init__(self, match):
        self.match = match

    def provide_commentary(self):
        match = self.match
        team1 = match.team1
        team2 = match.team2
        umpire = match.umpire

        # commentary 
        commentary = f"Team 1: {team1.name} vs. Team 2: {team2.name}\n"
        commentary += f"Current Score: {umpire.scores}/{umpire.wickets} in {umpire.overs} overs\n"
    
        return commentary

class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire()
        self.commentator = Commentator(self)

    def start_match(self):
        self.team1.decide_batting_order()
        self.team2.decide_batting_order()
        self.team1.select_captain(random.choice(self.team1.players))
        self.team2.select_captain(random.choice(self.team2.players))
        self.commentator.provide_commentary()
        self.simulate_innings(self.team1, self.team2)

    def simulate_innings(self, batting_team, bowling_team):
        umpire = self.umpire
        for batsman in batting_team.batting_order:
            while umpire.wickets < 10:
                bowler = bowling_team.choose_bowler()
                outcome = umpire.predict_outcome(bowler, batsman)
                if outcome == "out":
                    umpire.wickets += 1
                    print(f"{batsman.name} is out!")
                    next_batsman = batting_team.send_next_batsman()
                    if next_batsman:
                        print(f"Next batsman: {next_batsman.name}")
                    else:
                        print("Innings over!")
                        break
                else:
                    runs = random.randint(0, 6)
                    batting_team.update_score(runs)
                    print(f"{batsman.name} scores {runs} runs!")
                decision = umpire.make_decision(bowler)
                if decision == "no_ball":
                    print("No-ball!")
                elif decision == "wide_ball":
                    print("Wide ball!")
                self.commentator.provide_commentary()

    def change_innings(self):
        batting_team, bowling_team = self.team2, self.team1
        self.simulate_innings(batting_team, bowling_team)

    def end_match(self):
        if self.team1.total_score > self.team2.total_score:
            winner = self.team1
        elif self.team2.total_score > self.team1.total_score:
            winner = self.team2
        else:
            winner = None
        return winner


    
team1 = Team("Team 1", [Player("M S Dhoni", 0.8, 0.2, 0.99, 0.8, 0.9),
                         Player("Virat Kholi", 0.7, 0.3, 0.95, 0.7, 0.8),
                         Player("Rohith sharma", 0.6, 0.4, 0.9, 0.6, 0.7)])

team2 = Team("Team 2", [Player("ABD", 0.8, 0.2, 0.99, 0.8, 0.9),
                         Player("Maxwell", 0.7, 0.3, 0.95, 0.7, 0.8),
                         Player("Chris", 0.6, 0.4, 0.9, 0.6, 0.7)])

# Create field
field = Field(1.2, 0.9, 0.8, 1.1)

# Create match
match = Match(team1, team2, field)


match.start_match()

team1_total_score = match.team1.total_score
print(f"Team 1 total score: {team1_total_score}")

match.change_innings()
team2_total_score = match.team2.total_score
print(f"Team 2 total score: {team2_total_score}")

winner = match.end_match()
if winner:
    print(f"The winner is {winner.name}!")
else:
    print("The match ended in a draw.")






