from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'makeBelieve1'# set a secret key for security purposes
#template renders number of times client has visited site

#Start session at 1 count
# When the browser is refreshed increase by 1
@app.route('/')
def index():
    print('Get Counter Info')
    if 'count'not in session:
        session['count'] = 0 
    session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.pop('count')
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
