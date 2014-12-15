Feature: Compute all the scores from all the teams
		 As a scorer, I want to compute all of the scores of the team
		
		 @compute
		 Scenario: Compute all the scores
		 Given all the teams are set
		 Then I see scores
		 |team1_score|team2_score|
		 |2          |0          |