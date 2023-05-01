from datetime import datetime, timedelta, timezone

d = datetime.now().astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d")

print(d)