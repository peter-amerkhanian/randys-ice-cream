import csv

schedule_raw = []

# Open .csv and reduce to list of lists
with open("static/schedule.csv", mode="r") as f:
    schedule_csv = csv.reader(f)
    fields = next(schedule_csv)
    for row in schedule_csv:
        schedule_raw.append(row)

# Make into html text
schedule_cleaned = []

for day in schedule_raw:
    if day[2]:
        link = day[2]
        # Catch when http is not included
        if link.startswith("https://") or link.startswith("http://"):
            print('ok')
            # OK
            schedule_cleaned.append(f'<a href="{link}" target="_blank"> {day[0]} {day[1]}</a>')
        else:
            # Missing HTTP
            link_ammended = f"https://{link}"
            schedule_cleaned.append(f'<a href="{link_ammended}" target="_blank"> {day[0]} {day[1]}</a>')
    else:
        schedule_cleaned.append(f"{day[0]} {day[1]}")

print(schedule_cleaned)