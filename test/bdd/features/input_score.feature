Feature: Allow the scorer to input a point to a player for a team.
		 As a scorer, I want to put a point to a player who scored
		 
		 Scenario: A player scored
		 Given that a player "Eden Hazard" scored from team "Chelsea"
		 And that the player scored 2 points
		 |player_name|point_score|team   |
		 |Eden Hazard|2           |Chelsea|
		 When I hit submit 
		 Then the player "Eden Hazard" score was been tallied.