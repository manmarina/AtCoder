from datetime import datetime, timedelta

K = int(input())

base_time = datetime.strptime("21:00", "%H:%M")
after_time = base_time + timedelta(minutes=K)
print(after_time.strftime("%H:%M"))
