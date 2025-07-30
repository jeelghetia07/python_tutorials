from datetime import date as dt
dates = [(1,1,2025), (5,3,2025) ]

d1 = dates[0]
d2 = dates[1]
# d3 = dates[3]

date1 = dt(d1[2], d1[1] , d1[0])
date2 = dt(d2[2], d2[1] , d2[0])

days_diff = abs((date1 - date2).days)
print(days_diff)

# Output : 
# 63

# dictonary , set , functions 8140265898