'''
    "Valid Working Time"

    Write a function called valid_working_time that has the following parameters:
      work_time = The amount of hours worked in the day (integer)
      weekday = Whether the day is a weekday or not (boolean)
      holiday = Whether the day is a holiday or not (boolean)
    
    - On weekdays work time should be at least 8 hours and no more than 12 hours.
    - On weekends work time should be at least 4 hours and no more than 6 hours.
    - On holidays there should be no work time, unless the holiday is on a weekend,
    in which case the weekend work time rule applies.

    Return True if the work_time entered is valid and False if it isn't

    Examples:
        valid_working_time(10, True, False) --> True
        valid_working_time(10, True, True) --> False
        valid_working_time(4, False, True) --> True
        valid_working_time(2, True, True) --> False
'''

#Write your function under here
def valid_working_time(work_time,weekday,holiday):
  work = False
  if weekday:
    if work_time >= 8 and work_time <= 12 and not holiday:
      work = True
  if not weekday:
    if work_time >= 4 and work_time <= 6:
      work = True
  return work    
  
print(valid_working_time(10, True, True))
