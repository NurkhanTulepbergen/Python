from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print("Yesterday was: ", yesterday)
print("Current date: ", date.today())
print("Tommorow will be: ", tomorrow)