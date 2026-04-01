import os
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, session, url_for


def load_env_file():
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return

    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


load_env_file()

app = Flask(__name__, template_folder=".", static_folder="static")
app.secret_key = "replace-this-with-a-strong-secret-key"

LOGIN_USERNAME = os.environ.get("LOGIN_USERNAME", "admin")
LOGIN_PASSWORD = os.environ.get("LOGIN_PASSWORD", "adminPswd")


@app.route("/", methods=["GET", "POST"])
def login():
    if session.get("username"):
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Please enter both username and password.", "error")
            return render_template("index.html", logged_in=False, username=username)

        if username == LOGIN_USERNAME and password == LOGIN_PASSWORD:
            session["username"] = username
            flash("Login successful.", "success")
            return redirect(url_for("dashboard"))

        flash("Invalid username or password.", "error")
        return render_template("index.html", logged_in=False, username=username)

    return render_template("index.html", logged_in=False, username="")


@app.route("/dashboard")
def dashboard():
    username = session.get("username")
    if not username:
        flash("Please log in to continue.", "error")
        return redirect(url_for("login"))

    return render_template("index.html", logged_in=True, username=username)


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
