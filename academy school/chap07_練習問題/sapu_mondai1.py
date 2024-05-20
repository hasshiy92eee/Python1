from datetime import datetime

today = datetime.today()

end_of_year = datetime(today.year, 12, 31)

days = (end_of_year - today).days

print(f"今年は残り{days}日(;´･ω･)")