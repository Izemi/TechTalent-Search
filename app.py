import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///pjd.db")


@app.route("/")
@login_required
def index():
    """Show list of programming jobs"""
    jobs = db.execute("SELECT * FROM ProgrammingJobs")
    return render_template("index.html", jobs=jobs)


@app.route("/search", methods=["GET"])
@login_required
def search():
    keyword = request.args.get(
        "keywords"
    )  # This matches the 'name' attribute of your form's select element.
    location = request.args.get("location")

    # Add wildcards for partial matching
    keyword_search = f"%{keyword}%" if keyword else "%"
    location_search = f"%{location}%" if location else "%"

    # Execute the database query to find matching jobs
    jobs = db.execute(
        "SELECT * FROM ProgrammingJobs WHERE JobTitle LIKE ?", (keyword_search,)
    )

    # Render a template with the search results
    return render_template("search_results.html", jobs=jobs)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("MISSING USERNAME")

        if not request.form.get("password"):
            return apology("MISSING PASSWORD")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?;", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Get user inputs from the form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username and passwords are provided
        if not username:
            return apology("Missing username")
        elif not password or not confirmation:
            return apology("Missing password")
        elif password != confirmation:
            return apology("Passwords do not match")

        # Check if the username already exists in the database
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing_user:
            return apology("Username already exists")

        # Insert the new user into the database
        hashed_password = generate_password_hash(password)
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            hashed_password,
        )

        flash("Registered successfully!")
        return redirect(
            "/login"
        )  # Redirect to the login page after successful registration
    else:
        return render_template("register.html")


@app.route("/reset", methods=["GET", "POST"])
@login_required
def reset():
    if request.method == "POST":
        if not (password := request.form.get("password")):
            return apology("MISSING OLD PASSWORD")

        rows = db.execute("SELECT * FROM users WHERE id = ?;", session["user_id"])

        if not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("INVALID PASSWORD")

        if not (new_password := request.form.get("new_password")):
            return apology("MISSING NEW PASSWORD")

        if not (confirmation := request.form.get("confirmation")):
            return apology("MISSING CONFIRMATION")

        if new_password != confirmation:
            return apology("PASSWORD NOT MATCH")

        db.execute(
            "UPDATE users set hash = ? WHERE id = ?;",
            generate_password_hash(new_password),
            session["user_id"],
        )

        flash("Password reset successful!")

        return redirect("/")
    else:
        return render_template("reset.html")


@app.route("/job/<int:job_id>")
@login_required
def job(job_id):
    """Display details of a specific job."""
    job_details = db.execute("SELECT * FROM ProgrammingJobs WHERE JobID = ?", job_id)
    if not job_details:
        flash("Job not found.")
        return redirect("/")
    return render_template("job.html", job=job_details[0])


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run(debug=True)
