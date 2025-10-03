from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

CHOICES = ["Rock", "Paper", "Scissors"]

def get_winner(player, computer):
    """Determine the winner of a Rock-Paper-Scissors game"""
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def get_score():
    """Get current score from session, initialize if not exists"""
    if 'score' not in session:
        session['score'] = {'wins': 0, 'losses': 0, 'ties': 0}
    return session['score']

def get_game_history():
    """Get game history from session, initialize if not exists"""
    if 'game_history' not in session:
        session['game_history'] = []
    return session['game_history']

def add_to_history(player_choice, computer_choice, result):
    """Add a game to the history"""
    history = get_game_history()
    game_entry = {
        'player': player_choice,
        'computer': computer_choice,
        'result': result,
        'timestamp': len(history) + 1  # Simple counter for display
    }
    history.append(game_entry)

    # Keep only last 5 games
    if len(history) > 5:
        history.pop(0)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    player_choice = None
    computer_choice = None
    score = get_score()
    game_history = get_game_history()

    if request.method == "POST":
        # Handle both old dropdown and new button form structures
        player_choice = request.form.get("choice")

        if not player_choice or player_choice not in CHOICES:
            result = "Please select a valid choice!"
        else:
            computer_choice = random.choice(CHOICES)
            result = get_winner(player_choice, computer_choice)
            update_score(result)
            add_to_history(player_choice, computer_choice, result)

            # Update score and history for template
            score = get_score()
            game_history = get_game_history()

    return render_template("index.html",
                           result=result,
                           player_choice=player_choice,
                           computer_choice=computer_choice,
                           choices=CHOICES,
                           score=score,
                           game_history=game_history)

@app.route("/reset")
def reset_score():
    """Reset the game score and history"""
    session.pop('score', None)
    session.pop('game_history', None)
    return index()

if __name__ == "__main__":
    app.run(debug=True)
