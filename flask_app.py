
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from markupsafe import Markup
from get_hours import schedule_cleaned
import os.path


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/order')
def order():
    promo = os.path.isfile(os.path.abspath("static/Promo.png")) and os.path.isfile(os.path.abspath("static/Promo.png"))
    print(promo)
    schedule = Markup("<br>".join(schedule_cleaned).strip("<br>"))
    return render_template("order.html", schedule=schedule, promo=promo)


if __name__ == "__main__":
    app.run(debug=True)