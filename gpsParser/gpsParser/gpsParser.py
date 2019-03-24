# Created by Fayez Joseph Chedid

# You'll need to install this package via pip install gpsd-py3 then you may need to restart the IDE
import gpsd
import time
from math import sin, cos, sqrt, atan2, radians

# IP of the OBU
device = "192.168.50.78"

print('Waiting for a connection')
# Set parameters
gpsd.connect(host=device)

print("Parsing GPS information...")

while True:
    # Opens the modifier.txt (The path is relative so make sure the script and the modifier are in the same directory
    f = open("modifier.txt")
    modx = f.read()
    mod = int(modx)

    # Get the current position
    gpsLocation = gpsd.get_current()

    # Output for debugging
    print("This is my latitude", gpsLocation.lat)
    print("This is my longitude", gpsLocation.lon)
    # Gets time in local time must have True passed in the method
    print("This is my time", gpsLocation.get_time(True))

    # Approximate radius of Earth in km
    R = 6378.1

    # Setting the two latitudes and longitudes
    lat1 = radians(abs(gpsLocation.lat))
    lon1 = radians(abs(gpsLocation.lon))

    # These are Azrieli Pavillions Coordinates
    lat2 = radians(abs(45.382796))
    lon2 = radians(abs(-75.698951))

    # Calculating the difference
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Using Haversine formula to calculates the distance between the two points and prints in km
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    print("Result:", abs(distance*mod), "km")

    # Set this to double check between it and the distance displayed above
    print("Should be:", 12.79, "km")

    # Update the time it refreshes (in seconds)
    time.sleep(1)
