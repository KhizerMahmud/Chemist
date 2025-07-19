# app.py
from flask import Flask, render_template, request, redirect, session, url_for
import random
import time

app = Flask(__name__)
app.secret_key = 'chemistry_is_cool'

@app.route('/')
def index():
    session['target'] = random.randint(1, 20)
    session['attempts'] = 0
    session['score'] = session.get('score', 0)
    session['start_time'] = time.time()
    return redirect(url_for('play'))

@app.route('/play', methods=['GET', 'POST'])
def play():
    feedback = None
    phrase = None
    remaining_time = max(0, 60 - int(time.time() - session['start_time']))

    if remaining_time == 0:
        feedback = "Time's up! The lab exploded!"
        phrase = "Better luck next experiment."
        session['score'] = 0
        return render_template('game.html', feedback=feedback, phrase=phrase, time_left=remaining_time, score=session['score'])

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['attempts'] += 1
            target = session['target']

            if guess < target:
                feedback = "Too little acid! Reaction incomplete."
                phrase = random.choice(["Try adding more catalyst!", "Your flask bubbles faintly..."])
            elif guess > target:
                feedback = "Too much acid! Beaker overflow!"
                phrase = random.choice(["The compound fizzes violently!", "Dial it back, chemist!"])
            else:
                feedback = "Perfect! The compound is neutralized."
                phrase = random.choice(["Lab saved!", "Mission complete, Dr. Acid."])
                session['score'] += 1
                session['target'] = random.randint(1, 20)
                session['attempts'] = 0
                session['start_time'] = time.time()
        except ValueError:
            feedback = "Invalid input. Please enter a number."

    return render_template('game.html', feedback=feedback, phrase=phrase, time_left=remaining_time, score=session['score'])

if __name__ == '__main__':
    app.run(debug=True)