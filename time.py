from datetime import datetime, timedelta

MONTH = ['', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
TIMEZONES = {'LOS ANGELES' : -8.0, 'NEW YORK' : -5.0, 'CARACAS' : -4.5, 'BUENOS AIRES' : -3.0, 'LONDON' : 0.0, 'ROME' : 1.0, 'MOSCOW' : 3.0, 'TEHRAN' : 3.5, 'NEW DELHI' : 5.5, 'BEIJING' : 8.0, 'CANBERRA' : 10.0}

def time_difference(city_a, timestamp, city_b):
    mon, day, year, time = timestamp.replace(',',' ').split()
    hh, mm=time.replace(':',' ').split()
    mon = MONTH.index(mon.upper()[:3])
    time_diff = TIMEZONES[city_b.upper()] - TIMEZONES[city_a.upper()]
    add_min = time_diff * 60
    return (datetime(int(year),mon,int(day),int(hh),int(mm)) + timedelta(minutes = add_min)).strftime('%Y-%m-%d %H:%M')

print(time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra"))