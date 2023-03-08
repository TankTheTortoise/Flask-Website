from datetime import timedelta, datetime
from testing import chuck_joke, random_chuck, nasaPictureDay, randomDate, addDay
from flask import Flask, render_template, request, flash, session, redirect, url_for
import sqlalchemy
from flask_sqlalchemy.session import Session

coins = "https://www.youtube.com/embed/zFZ5jQ0yuNA"
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
        'likes': 1,
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018',
        'likes': 0,
    }
]

app = Flask(__name__)
app.secret_key = "Secret Key"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html")


@app.route("/chuck", methods=["POST", "GET"])
def chuck():
    if request.method == "POST":
        chucks = int(request.form["num"])
        jokes = [chuck_joke() for x in range(chucks)]
        images = random_chuck(int(chucks))
        times = int(chucks)
        return render_template("jokes.html", jokes=jokes, images=images, times=times)

    return render_template("chuck.html", posts=posts)


@app.route("/jokers/<int:chucks>")
def jokers(chucks):
    jokes = [chuck_joke() for x in range(chucks)]
    images = random_chuck(int(chucks))
    times = int(chucks)
    return render_template("jokes.html", jokes=jokes, images=images, times=times)


@app.route("/nasaPic", methods=["GET", "POST"])
def nasaPic():
    if request.method == 'POST':
        if request.form["submit"] == "Random date":
            params = randomDate()
            tt = nasaPictureDay(params)
            date = tt['date']
            explanation = tt['explanation']
            title = tt['title']
            url = tt['url']
            #next = addDay(date, rand=False)
            return render_template("nasaPic.html", date=date, explanation=explanation, title=title, url=url, next=next)

        elif request.form["submit"] == "Fetch Image":
            params = request.form["datedate"]
            tt = nasaPictureDay(params)
            date = tt['date']
            explanation = tt['explanation']
            title = tt['title']
            url = tt['url']

        elif request.form["submit"] == "Next Day":
            time = request.form["dated"]
            tt = nasaPictureDay(addDay(time))
            date = tt['date']
            explanation = tt['explanation']
            title = tt['title']
            url = tt['url']

        else:
            params = datetime.today().strftime('%Y-%m-%d')
            tt = nasaPictureDay(params)
            date = tt['date']
            explanation = tt['explanation']
            title = tt['title']
            url = tt['url']

        return render_template("nasaPic.html", date=date, explanation=explanation, title=title, url=url)


@app.route("/nasa")
def nasa():
    date = datetime.today().strftime('%Y-%m-%d')
    return render_template("nasa.html", date=date)


if __name__ == "__project__":
    app.run(host='0.0.0.0', port=5000, debug=True)
