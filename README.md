# Cricket Match Simulator
This is a cricket match simulator program that allows you to simulate a cricket match between two teams. The program includes various classes representing different aspects of the game, such as players, teams, field, umpire, commentator, and the match itself.

**Classes**


Player: Represents a cricket player with attributes like name, batting ability, bowling ability, fielding ability, running ability, and experience.

Team: Represents a cricket team with attributes like name, a list of players, captain, batting order, and total score. It has methods to select a captain, send the next batsman, choose a bowler, decide batting order, and update the score.

Field: Represents the cricket field with attributes like size, fan ratio, pitch conditions, and home advantage. It has a method to calculate the probability of a player's performance based on field conditions.

Umpire: Represents the umpire in a cricket match with attributes like scores, wickets, and overs. It has methods to predict the outcome of a ball (out or not out) and make decisions (normal, no ball, wide ball).

Commentator: Represents a commentator in a cricket match. It takes the match object as input and provides commentary based on the match situation.

Match: Represents a cricket match between two teams. It has attributes like team1, team2, field, umpire, and commentator. It has methods to start the match, simulate innings, change innings, and end the match.


**Algorithm**
The match simulation algorithm follows these steps:

Create two teams (team1 and team2) with their respective players.

Create a field with specified attributes like size, fan ratio, pitch conditions, and home advantage.

Create a match object with team1, team2, and the field.

Start the match by deciding the batting order for both teams and selecting captains.

Simulate the innings of team1. For each batsman, choose a random bowler from team2 and predict the outcome (out or not out) based on the probabilities of the batsman and bowler. Update the score accordingly and make decisions (normal, no ball, wide ball) based on the bowler's ability. Provide commentary after each ball.

Change innings and simulate the innings of team2 following the same process as in step 5.

End the match and determine the winner based on the total scores of both teams.

**Sample Run Cases**
Case 1: Team 1 wins
Team 1: M S Dhoni, Virat Kohli, Rohit Sharma

Team 2: ABD, Maxwell, Chris

Rohith sharma is out!
Next batsman: Rohith sharma
Rohith sharma is out!
Next batsman: M S Dhoni
Rohith sharma scores 1 runs!
No-ball!
Rohith sharma scores 2 runs!
No-ball!
Rohith sharma is out!
Next batsman: Virat Kholi
Rohith sharma scores 4 runs!
Rohith sharma scores 2 runs!
Rohith sharma scores 3 runs!
Rohith sharma scores 3 runs!
Rohith sharma scores 5 runs!
Rohith sharma is out!
Innings over!
Team 1 total score: 20
ABD scores 2 runs!
ABD scores 4 runs!
No-ball!
ABD scores 3 runs!
ABD is out!
Next batsman: ABD
Team 2 total score: 9
The winner is Team 1!

**Conclusion**
This cricket match simulator allows you to simulate a cricket match between two teams, providing commentary and determining the winner based on the total scores. You can customize the teams, players, and field attributes to create different scenarios and enjoy a virtual cricket match.
