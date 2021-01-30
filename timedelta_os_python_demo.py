"""
from datetime import datetime,timedelta

current_datetime = datetime.now()

#future dates
one_year_future = current_datetime + timedelta(days=365)
print(one_year_future)

#past_dates
pastdate = current_datetime - timedelta(days=3)
print(pastdate)


dt=current_datetime.date()
print(dt)

tomorrow=dt+timedelta(days=1)
print(tomorrow)
"""

import os
split_up=os.path.splitext("demo.txt")
print(split_up)

file_name=split_up[0]
file_extension=split_up[1]

print(file_name,file_extension)
