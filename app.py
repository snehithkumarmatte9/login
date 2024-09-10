from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy users
users = {'admin': 'admin123', 'user': 'user123'}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if admin
        if username == 'admin' and password == users['admin']:
            session['user_type'] = 'admin'
            return redirect(url_for('admin_dashboard'))
        # Check if regular user
        elif username == 'user' and password == users['user']:
            session['user_type'] = 'user'
            return redirect(url_for('user_dashboard'))
        else:
            return "Invalid credentials, try again!"
    return render_template('login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_type' in session and session['user_type'] == 'admin':
        return render_template('admin_dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/user_dashboard')
def user_dashboard():
    if 'user_type' in session and session['user_type'] == 'user':
        return render_template('user_dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_type', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
