for i in range(1,25):
    if(1 <= i <= 11):
        print(f"{i}:00 AM")
    elif(i == 12):
        print(f"{i}:00 NOON")
    elif(13 <= i <= 23):
        print(f"{i}:00 PM")
    elif(i == 24):
        print(f"{i}:00 MIDNIGHT")

# Output : 
# 1:00 AM
# 2:00 AM
# 3:00 AM
# 4:00 AM
# 5:00 AM
# 6:00 AM
# 7:00 AM
# 8:00 AM
# 9:00 AM
# 10:00 AM
# 11:00 AM
# 12:00 NOON
# 13:00 PM
# 14:00 PM
# 15:00 PM
# 16:00 PM
# 17:00 PM
# 18:00 PM
# 19:00 PM
# 20:00 PM
# 21:00 PM
# 22:00 PM
# 23:00 PM
# 24:00 MIDNIGHT