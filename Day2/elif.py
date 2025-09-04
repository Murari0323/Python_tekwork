def findWeek(a):
    if(a==1):
        return "sunday"
    elif a==2:
        return "monday"
    elif a==3:
        return "tuesday"
    elif a==4:
        return "wednesday"
    elif a==5:
        return "thursday"
    elif a==6:
        return "friday"
    elif a==7:
        return "saturday"
    else:
        return "invalid week number"

weeknum=int(input("Enter the week number: "))
print(findWeek(weeknum))
