from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1

    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1
    return render_template('index.html', count=session['count'], visits=session['visits'])


@app.route('/increment', methods=['POST'])
def increment():
    if 'custom_increment' in request.form:
        session['custom_increment'] = request.form["custom_increment"]
        session['count'] += int(session['custom_increment'])
        session['visits'] -= 1
    elif 'increment_by_two' in request.form:
        session['count'] += 2
        session['visits'] -= 1
    elif 'increment_by_one' in request.form:
        session['count'] += 1
        session['visits'] -= 1
    return redirect('/')


@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
