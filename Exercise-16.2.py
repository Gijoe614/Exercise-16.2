
class Time:
    """
    """

    def __init__(self):
        pass


#
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

#
def is_after(t1, t2):
    seconds1 = time_to_int(t1)
    seconds2 = time_to_int(t2)
    difference = seconds2 - seconds1
    return [" follows ", " does not follow "][difference >= 0]

#
time1 = Time()
time1.hour = 20
time1.minute = 12
time1.second = 9


time2 = Time()
time2.hour = 8
time2.minute = 3
time2.second = 18


time1.seconds = time_to_int(time1)

time2.seconds = time_to_int(time2)

result = is_after(time1, time2)

print ('Time 1 = ' + '%.2d:%.2d:%2d' % (time1.hour, time1.minute, time1.second))
print ('\nTime 2 = ' + '%.2d:%.2d:%2d' % (time2.hour, time2.minute, time2.second))
print ('\n%.2d:%.2d:%.2d' % (time1.hour, time1.minute, time1.second) + result + '%.2d:%.2d:%.2d' % (time2.hour, time2.minute, time2.second) + ' chronologically.')
