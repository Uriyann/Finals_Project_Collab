import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)

# Just the current date
today = datetime.date.today()
print("Today:", today)

# Create a specific date
my_birthday = datetime.date(2005, 8, 7)
print("My Birthday:", my_birthday)

# Format date
formatted = now.strftime("%B %d, %Y - %I:%M %p")
print("Formatted:", formatted)

# Difference between dates
future_date = datetime.date(2025, 12, 25)
days_left = (future_date - today).days
print("Days until Christmas 2025:", days_left)

now