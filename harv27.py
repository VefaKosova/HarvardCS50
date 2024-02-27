import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("text/students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    # writer = csv.writer(file)
    writer.writerow({"name": name, "home": home})
    # writer.writerow([name, home])