from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

QUESTIONS = [
    "Does your child avoid eye contact?",
    "Does your child don't respond to their name?",
    "Does your child repeat the same actions?",
    "Does your child prefer to play alone?",
    "Does your child have delayed speech?",
    "Does your child react strongly to sounds?",
    "Does your child find it hard to understand emotions?",
    "Does your child get upset with small changes?"
]

def get_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "database.db")
    conn = sqlite3.connect(DB_PATH)    
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        child_name = request.form["child_name"]
        score = 0

        for i in range(len(QUESTIONS)):
            if request.form.get(f"q{i}") == "yes":
                score += 1

        if score <= 2:
            risk = "Low Risk"
        elif score <= 4:
            risk = "Mild Risk"
        elif score <= 6:
            risk = "Moderate Risk"
        else:
            risk = "High Risk"

        conn = get_db()
        conn.execute(
            "INSERT INTO responses (child_name, total_score, risk_level) VALUES (?, ?, ?)",
            (child_name, score, risk)
        )
        conn.commit()

        data = conn.execute("SELECT * FROM responses").fetchall()
        conn.close()

        return render_template(
            "result.html",
            score=score,
            risk=risk,
            records=data
        )

    return render_template("index.html", questions=QUESTIONS)

if __name__ == "__main__":
    app.run(debug=True)