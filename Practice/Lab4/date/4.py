from datetime import datetime, timedelta

today=datetime.now()
another_date=datetime.strptime("22-January-2024,07:00:00","%d-%B-%Y,%H:%M:%S")

difference=(today-another_date).total_seconds()
print(difference)