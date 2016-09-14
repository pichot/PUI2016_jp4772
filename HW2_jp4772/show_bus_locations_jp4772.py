from __future__ import print_function
import json
import urllib2
import sys

key = sys.argv[1]
bus_number = sys.argv[2]

api_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&version=2&LineRef=%s" % (key, bus_number)
response = urllib2.urlopen(api_url)
data = json.loads(response.read().decode("utf-8"))
vehicles = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

vehicle_count = len(vehicles)

print ("Bus Line : %s" % (bus_number))
print ("Number of Active Buses : %s" % (vehicle_count))

for idx, vehicle in enumerate(vehicles):
    lat = vehicle["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    lon = vehicle["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    print ("Bus %s is at latitude %s and longitude %s" % (idx, lat, lon))
