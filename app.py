from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secretkey"

users = {}

@app.route("/")
def home():
    return redirect("/login")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users[username] = password

        return redirect("/login")

    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect("/dashboard")

        return "Invalid Username or Password"

    return render_template("login.html")

# Dashboard
@app.route("/dashboard")
def dashboard():

    if "user" in session:
        return render_template("dashboard.html", name=session["user"])

    return redirect("/login")

# Logout
@app.route("/logout")
def logout():

    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)