# This program compares the effect of driving at different speeds on your fuel
# consumption.The user will enter the distance of their drive in kilometers and
# the cost of gas per liter.The program will report back the cost of doing that
# drive atdifferent speeds.
distance = float(input("How long is your daily drive in Kilometers? "))
cost_perLiter = float(input("How much does gas cost per liter? "))
milespergallon = float(input("What is your car's kilometer per litre rating? "))
# 0.6 mile = 1 Kilometer, 1 US gallon = 3.78 L, approximately
# convert miles per gallon to kilometers per liter
kilometerpergallon = milespergallon / 0.6 / 3.78
# milage tables start at 55mph, need to convert to kph
cost_perday = cost_perLiter * (distance / kilometerpergallon)
cost_at100 = round ( cost_perday * 1.03, 2)
print ("\nIf you drive at " + str(60 * 1.6)+" km/h it will cost $" +
str (cost_at100)+" per day")
print ("That's $"+str(round(cost_at100*365.4,2))+" per year.\n")

cost_at120 = round( cost_perday * 1.23, 2)
print ("If you drive at " + str(75 * 1.6)+" km/h it will cost $"+
str( cost_at120)+" per day")
print("That's $"+str(round(cost_at120 * 365.4,2))+" per year.\n")
print ("That's a difference of " +
str( round( ( cost_at120 - cost_at100 ) * 365.4, 2 ) ) +\
" per year to drive 20 km/h faster." )
# how many minutes to drive dist at 100 kph?
time_ToDriveAt100 = distance * ( 60 / 100 )
# how many minutes to drive dist at 120 kph?
time_ToDriveAt120 = distance * ( 60 / 120 )
timeDiff = time_ToDriveAt100 - time_ToDriveAt120
print ("You save " + str(timeDiff) + " minutes per day.")
