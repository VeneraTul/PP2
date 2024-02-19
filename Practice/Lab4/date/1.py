from datetime import datetime,timedelta 

today=input()
data=datetime.strptime(today,'%Y-%m-%d')
current_data=data- timedelta(days=5)

print(current_data.strftime('%Y-%m-%d'))
