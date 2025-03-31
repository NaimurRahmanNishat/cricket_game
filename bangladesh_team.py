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





# using graphical user interface
import tkinter as tk
import random as rd

class CricketGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bangladesh Team Batting")

        self.score = 0
        self.balls_remaining = 60
        self.current_player = 0

        self.players = [
            "Liton Dak", "Soumya Sarkar", "Loard King Shanto", "Towhid Hridoy", "Jaker Ali Anik", 
            "Shamim Hassan Patuary", "Nurul Hasan Nahid", "Rishad Hossain", "Mahadi Hasan", 
            "Nahid Rana", "Mustafizur Rahman"
        ]
        
        self.player_scores = {player: 0 for player in self.players}
        self.current_player_name = self.players[self.current_player]
        
        self.label = tk.Label(root, text=f"{self.current_player_name}'s Turn", font=("Arial", 16))
        self.label.pack()
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()
        
        self.submit_button = tk.Button(root, text="Play", command=self.play_turn, font=("Arial", 14))
        self.submit_button.pack()
        
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()
        
        self.score_label = tk.Label(root, text=f"Team Score: {self.score}", font=("Arial", 14))
        self.score_label.pack()

    def play_turn(self):
        if self.balls_remaining == 0 or self.current_player >= len(self.players):
            self.result_label.config(text="Game Over!")
            return
        
        try:
            player_score = int(self.entry.get())
            if player_score < 0 or player_score > 7:
                self.result_label.config(text="Invalid input! Enter 0 to 7")
                return
        except ValueError:
            self.result_label.config(text="Invalid input! Enter a number (0 to 7)")
            return
        
        bowler_ball = rd.randint(0, 6)
        self.result_label.config(text=f"Bowler's Delivery: {bowler_ball}")
        
        if player_score == bowler_ball:
            self.result_label.config(text=f"{self.current_player_name} is OUT! Scored: {self.player_scores[self.current_player_name]}")
            
            if self.player_scores[self.current_player_name] >= 50:
                self.result_label.config(text=f"Congratulations {self.current_player_name} for scoring a half-century!")
            if self.player_scores[self.current_player_name] >= 100:
                self.result_label.config(text=f"Congratulations {self.current_player_name} for scoring a century!")
            
            # Special Messages for players scoring 0 runs
            if self.player_scores[self.current_player_name] == 0:
                if self.current_player_name == "Liton Dak":
                    self.result_label.config(text="🚨 বাবা ডাক! তুই কোন পাপের শাস্তি দিচ্ছিস রে!")
                elif self.current_player_name == "Soumya Sarkar":
                    self.result_label.config(text="🤣 ধন্যবাদ সুমাইয়া আপা, আপনি আপনার আগের ফর্মে ফিরে গেছেন!")
                elif self.current_player_name == "Loard King Shanto":
                    self.result_label.config(text="👑 বাংলাদেশের কিং, দ্য ব্লুটুথ বয় মিস্টার গোল্ডেন লর্ড কিং শান্ত!")

            self.current_player += 1
            if self.current_player < len(self.players):
                self.current_player_name = self.players[self.current_player]
                self.label.config(text=f"{self.current_player_name}'s Turn")
        else:
            self.score += player_score
            self.player_scores[self.current_player_name] += player_score
        
        self.balls_remaining -= 1
        self.score_label.config(text=f"Team Score: {self.score}")
        self.entry.delete(0, tk.END)
        
        if self.balls_remaining == 0 or self.current_player >= len(self.players):
            self.show_final_scorecard()

    def show_final_scorecard(self):
        scorecard = "\n🏏 Final Scorecard:\n"
        for player, runs in self.player_scores.items():
            scorecard += f"{player}: {runs} runs\n"
        scorecard += f"\n🏏 Bangladesh Final Score: {self.score} runs"
        self.result_label.config(text=scorecard)

root = tk.Tk()
app = CricketGame(root)
root.mainloop()