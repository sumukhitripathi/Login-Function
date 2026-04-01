from flask import Flask, request, url_for, redirect, Response, session

app = Flask(__name__)
app.secret_key = "sams_secret_key"  # Set a secret key for session management

@app.route("/", methods=["GET", "POST"])

def login():
    if request.method == "POST":
        usename = request.form["username"]
        password = request.form["password"]
        if usename == "admin" and password == "admin":
            session["username"] = usename  #store username in session
            return redirect(url_for("home"))
        else:
            return Response("Invalid username or password", mimetype="text/plain")
        
    return '''
        <h2>Login Page</h2>
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/home")
def home():
    if "username" in session:
        return f'''
            <h2>Welcome, {session['username']}!</h2>
            <a href="{url_for('logout')}">Logout</a>
        '''
    else: