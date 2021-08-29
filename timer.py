import datetime

start = "2021-08-24 01:00:00.000000"

with open('timer.txt', 'r') as timesince:
    end = timesince.readline().rstrip()
    delta = datetime.datetime(2021, 8, 27) - datetime.datetime.now()
    print('End date: ', end)
    print (delta)

    # delta = datetime(year=2011, month=05, day=05) - datetime(year=now.year, month=now.month, day=now.day, minute=now.minute)


