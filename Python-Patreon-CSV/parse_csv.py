import csv

#Generate an HTML file from the csv file

html_output = ''
names = []
with open('patrons.csv', 'r') as cf:
    csv_file = csv.DictReader(cf)

    #skipping the unwanted first line
    next(csv_file)

    for lines in csv_file:
        if lines['FirstName'] == 'No Reward':
            break
        names.append(f"{lines['FirstName']} {lines['LastName']}")

html_output = f"There are currently {len(names)} contributors"
html_output += "\n<ul>"
for name in names:
    html_output += f"\n\t<li>{name}</li>"

html_output += "\n</ul>"

with open('patrons.html', 'w') as hf:
    hf.write(html_output)
