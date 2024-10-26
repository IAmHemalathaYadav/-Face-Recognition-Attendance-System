 
from flask import Flask, request, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/take-attendance', methods=['GET', 'POST'])
def take_attendance():
    if request.method == 'POST':
        try: 
            subprocess.Popen(['python', 'back1.py'])  
            return 'Attendance process started.'
        except Exception as e:
            return str(e)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

