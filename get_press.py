import csv
import os.path
import pickle

press_raw = []

production = not os.path.isfile('static/LOGO-01.png')

if production:
    press_path = "/home/nbrandon62/randys-ice-cream/static/press.csv"
else:
    press_path = "static/press.csv"

if os.path.isfile(press_path):

    # Open .csv and reduce to list of lists
    with open(press_path, mode="r") as f:
        press_csv = csv.reader(f)
        fields = next(press_csv)
        for row in press_csv:
            press_raw.append(row)

    # Make into html text
    press_cleaned = []

    for item in press_raw:
        link = item[2]
        # Catch when http is not included
        if link.startswith("https://") or link.startswith("http://"):
            # HTTP included
            link_ammended = link
            press_cleaned.append(f'<p><a style="text-decoration: underline" href="{link_ammended}" target="_blank"><b>{item[0]}</b></a> - {item[1]}</p>')
        else:
            # Missing HTTP
            link_ammended = f"https://{link}"
            press_cleaned.append(f'<p><a style="text-decoration: underline" href="{link_ammended}" target="_blank"><b>{item[0]}</b></a> - {item[1]}</p>')

    press_cleaned = press_cleaned[::-1]
else:
    press_cleaned = None