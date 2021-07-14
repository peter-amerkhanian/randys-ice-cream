import csv
import os.path

schedule_raw = []

production = not os.path.isfile('static/LOGO-01.png')

if production:
    schedule_path = "/home/nbrandon62/randys-ice-cream/static/schedule.csv"
else:
    schedule_path = "static/schedule.csv"


if os.path.isfile(schedule_path):
    # Open .csv and reduce to list of lists
    with open(schedule_path, mode="r") as f:
        schedule_csv = csv.reader(f)
        fields = next(schedule_csv)
        for row in schedule_csv:
            schedule_raw.append(row)

    # Make into html text
    schedule_cleaned = []
    link_ammended = None

    for day in schedule_raw:
        if day[2]:
            link = day[2]
            # Catch when http is not included
            if link.startswith("https://") or link.startswith("http://"):
                link_ammended = link
                # OK
                schedule_cleaned.append(f'<a href="{link_ammended}" target="_blank"> {day[0]} {day[1]}</a>')
            else:
                # Missing HTTP
                link_ammended = f"https://{link}"
                schedule_cleaned.append(f'<a href="{link_ammended}" target="_blank"> {day[0]} {day[1]}</a>')
        else:
            schedule_cleaned.append(f"{day[0]} {day[1]}")
else:
    schedule_cleaned = None
    link_ammended = None