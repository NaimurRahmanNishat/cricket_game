import random as rd
def bangladesh_team_batting():
    score = 0  # Total team score
    balls_remaining = 60  # Total number of balls
    players = ["Liton Dak", "Soumya Sarkar", "Loard King Shanto", "Towhid Hridoy", "Jaker Ali Anik", "Shamim Hassan Patuary", "Nurul Hasan Nahid", "Rishad Hossain", "Mahadi Hasan", "Nahid Rana", "Mustafizur Rahman"]
    
    current_player = 0  # Index of the batsman at strike
    player_scores = {player: 0 for player in players}  # Dictionary to store runs for each player
    
    while balls_remaining > 0 and current_player < len(players):  
        player_name = players[current_player]  # Get the name of the current batsman

        try:
            player_score = int(input(f"{player_name} : "))
            if player_score < 0 or player_score > 7:
                print("Invalid input! Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        bowler_ball = rd.randint(0, 6)  # Random number for bowler’s delivery
        print(f"Bowler's Delivery: {bowler_ball}")

        if player_score == bowler_ball:  # Out condition
            print(f"{player_name} is OUT!")
            print(f"{player_name}'s Final Score: {player_scores[player_name]} runs")

            if player_scores[player_name] >= 50:
                print(f"Congratulations {player_name} for scoring a half-century!")
            if player_scores[player_name] >= 100:
                print(f"Congratulations {player_name} for scoring a century!")
            
            # Special Messages for players scoring 0 runs
            if player_scores[player_name] == 0:
                if player_name == "Liton Dak":
                    print("🚨 বাবা ডাক! তুই কোন পাপের শাস্তি দিচ্ছিস রে!")
                elif player_name == "Soumya Sarkar":
                    print("🤣 ধন্যবাদ সুমাইয়া আপা, আপনি আপনার আগের ফর্মে ফিরে গেছেন!")
                elif player_name == "Loard King Shanto":
                    print("👑 বাংলাদেশের কিং, দ্য ব্লুটুথ বয় মিস্টার গোল্ডেন লর্ড কিং শান্ত!")
            
            current_player += 1  # Move to the next player
        else:
            score += player_score  # Add to the team's score
            player_scores[player_name] += player_score  # Add to individual player's score
        
        balls_remaining -= 1  # Reduce remaining balls
    
    # Final Scorecard
    print("\n🏏 Bangladesh Team Final Scorecard:")
    for player, runs in player_scores.items():
        print(f"{player}: {runs} runs")

    print(f"\n🏏 Bangladesh Final Score: {score} runs")

# Run the game
bangladesh_team_batting()