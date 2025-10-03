from flask import Flask, render_template, request
import random

app = Flask(__name__)

CHOICES = ["Rock", "Paper", "Scissors"]

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    player_choice = None
    computer_choice = None

    if request.method == "POST":
        player_choice = request.form["choice"]
        computer_choice = random.choice(CHOICES)
        result = get_winner(player_choice, computer_choice)

    return render_template("index.html", 
                           result=result, 
                           player_choice=player_choice, 
                           computer_choice=computer_choice,
                           choices=CHOICES)

if __name__ == "__main__":
    app.run(debug=True)
