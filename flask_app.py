
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from markupsafe import Markup
from get_hours import schedule_cleaned, link_ammended, production
from get_press import press_cleaned
import os.path
import pickle


app = Flask(__name__)

if production:
    static_path = "/home/nbrandon62/randys-ice-cream/static/"
else:
    static_path = "static/"

print("Production: ", production)

@app.route('/')
def index():
    closed = os.path.isfile(f"{static_path}/closed.png")
    return render_template("index2.html", closed=closed)

@app.route('/about')
def about():
    if press_cleaned:
        press = Markup("".join(press_cleaned))
        pickle.dump( press, open( f"{static_path}backup_press.p", "wb" ) )
    else:
        press = pickle.load( open( f"{static_path}backup_press.p", "rb" ) )
    return render_template("about.html", press=press)

@app.route('/order')
def order():
    promo =  os.path.isfile(f"{static_path}Promo.png")
    promo_menu = os.path.isfile(f"{static_path}Promo Menu.png")
    promo_link = link_ammended
    print("promo:", promo)
    print("promo_menu:", promo_menu)
    print("link:", promo_link)
    if schedule_cleaned:
        schedule = Markup("".join(schedule_cleaned).strip("<br>"))
        pickle.dump( schedule, open( f"{static_path}backup_schedule.p", "wb" ) )
    else:
        schedule = pickle.load( open( f"{static_path}backup_schedule.p", "rb" ) )
    return render_template("order.html", schedule=schedule, promo=promo, promo_menu=promo_menu, promo_link=promo_link)


if __name__ == "__main__":
    app.run(debug=True)