heart_rate = int(input('Heart rate: '))
too_low = heart_rate < 60
too_high = heart_rate > 100
if too_low = True and too_high = False:
    print('Your heart rate is too low.')
elif too_high = True and too_low = False:
    print('Your heart rate is too high.')
else:
    print('Your heart are stable ')