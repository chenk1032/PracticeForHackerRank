def day_of_programmer(year):
    if year == 1918:
        return '26.09.1918'
    elif 1700 <= year <= 1917:
        if year % 4 == 0:
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)
    elif 1919 <= year <= 2700:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)





