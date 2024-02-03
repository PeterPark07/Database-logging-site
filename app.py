from flask import Flask, render_template, request, redirect, url_for
from database import notes
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    all_notes = notes.find()
    return render_template('index.html', notes=all_notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note_content = request.form['note_content']
    current_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")
    notes.insert_one({'content': note_content, 'timestamp': current_time})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
