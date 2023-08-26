'''
Samantha Ho
Project 5 Drop Assignment 
CS 130R
'''

#datetime (year, month, day, hour)
from datetime import datetime, timedelta
class Flight:
    def __init__(self,origin, dest, takeoff, duration):
        self.origin = origin
        self.dest = dest
        self.takeoff = takeoff
        self.duration = duration
        self.hours = 0
       

    def Origin(self):
        return self.origin

    def Destination(self):
        return self.dest

    def DepartureTime(self):
        departSelf = self.takeoff
        return departSelf
        
        
    def LandingTime(self):
        new = self.takeoff
        new += timedelta(hours = self.duration)
        return new

    def Conflict(self, other):
        f3Land = self.LandingTime()
        f3Depart = self.DepartureTime()
        f1Land = other.LandingTime()
        f1Depart = other.DepartureTime()
        return f1Land > f3Depart
       
    def ToString(self):
        x = self.DepartureTime()
        delta = self.LandingTime() - self.DepartureTime()
        return str(self.origin) + " to " + str(self.dest) + " on " + str(x) + " lasting " + str(delta)


f1 = Flight("LA", "NY", datetime(2019, 1,3,9), 5)
f2 = Flight("NY", 'Tokyo', datetime(2019, 1, 3, 12), 14)
f3 = Flight('NY', 'Tokyo', datetime(2019, 1, 3, 15), 14)

print(f1.ToString())
# LA to NY 2019-01-03 09:00:00 lasting 5:00:00

print(f3.ToString())

print(f1.Conflict(f1))
# True

print(f3.LandingTime())
# 2019-01-04 05:00:00

print(f3.Conflict(f1))
# False



