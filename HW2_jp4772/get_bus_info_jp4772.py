from __future__ import print_function
import json
import urllib2
import sys
import csv

key = sys.argv[1]
bus_number = sys.argv[2]
file_name = sys.argv[3]

api_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&version=2&LineRef=%s" % (key, bus_number)
response = urllib2.urlopen(api_url)
data = json.loads(response.read().decode("utf-8"))
vehicles = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

with open(file_name, 'wb') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["Latitude", "Longitude", "Stop Name", "Stop Status"])

    for vehicle in vehicles:
        lat = vehicle["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        lon = vehicle["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]

        status = vehicle["MonitoredVehicleJourney"]["MonitoredCall"]["ArrivalProximityText"]
        stop = vehicle["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointName"][0]

        if not status:
            status = "N/A"
        if not stop:
            stop = "N/A"

        csv_file.writerow([lat, lon, stop, status])
