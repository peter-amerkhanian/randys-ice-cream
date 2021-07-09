
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from markupsafe import Markup
from get_hours import schedule_cleaned, link_ammended, production
import os.path


app = Flask(__name__)

if production:
    static_path = "/home/nbrandon62/randys-ice-cream/static/"
else:
    static_path = "static/"

print(production)

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/order')
def order():
    promo =  os.path.isfile(f"{static_path}Promo.png")
    promo_menu = os.path.isfile(f"{static_path}Promo Menu.png")
    print("promo:", promo)
    print("promo_menu:", promo_menu)
    schedule = Markup("<br>".join(schedule_cleaned).strip("<br>"))
    return render_template("order.html", schedule=schedule, promo=promo, promo_menu=promo_menu, promo_link=link_ammended)


if __name__ == "__main__":
    app.run(debug=True)