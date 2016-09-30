# PUI2016 HW2 - jp4772

## Assignment 1
Wrote `show_bus_locations_jp4772.py` script. First, it collects the two arguments passed into the script (so much trust!). String interpolation into the URL for MTA's realtime API (is there a better way to interpolate in Python? I'm not a huge fan of the generic `%s`, any way to simple place the variable within the string a la Ruby:

```ruby
"This is #{interpolation} done #{beautifully}"
```

Anyway, after making the URL, the script requests the JSON, parses it, and then isolates the vehicles list into a variable. The length of that list is the vehicle count, which is printed with the requested bus number. Then the vehicle list is looped over, with the lat/lon of each bus printed in turn.

## Assignment 2
Creates a CSV of current vehicle locations and upcoming stops. Makes a request to the MTA API similar as above, then opens a CSV file using Python's built-in IO library, adds a header row to the CSV, then loops over the vehicles list, adding each row in turn per vehicle.

NOTE: I couldn't get the API to response with a missing `status` or `upcoming stop`, so I'm guessing that API will still return a complete JSON object but that those attributes will be blank. If they do come back blank (null or empty string), I have logic that will set the fields as `N/A` in the CSV. But if the JSON is missing those attributes entirely my script will crash. It would be helpful in future assignments to have an example of edge case returns if we're to account for them but can't reproduce them on the API itself.

## Assignment 3
The more interesting notes are contained within my notebook, but this took the most time as I had to learn more about pandas (which was awesome).
