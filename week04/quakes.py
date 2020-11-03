
# At the top of the file, import any libraries you will use.
# import ...
import requests
import json
# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):

# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...
    # import the data
    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                        params={
                            'starttime': "2000-01-01",
                            "maxlatitude": "58.723",
                            "minlatitude": "50.008",
                            "maxlongitude": "1.67",
                            "minlongitude": "-9.756",
                            "minmagnitude": "1",
                            "endtime": "2018-10-11",
                            "orderby": "time-asc"}
                        )
    #quakes.text[0:100]

    # parse the data as JSON
    data = json.loads(quakes.text)

    #print(data.keys()) # gives the keys
    #print(data['features'][0].keys()) # gives keys to features in first quake
    #print(data['features'][0]['properties'].keys()) # gives keys in properties
    #print(data['features'][0]['properties']['mag']) # gives magnitude of first quake

    # finding the largest quake

    # get the features key section of the quakes
    quakes = data['features']

    # property to find largest
    largest = quakes[0] # initialise as first quake
    # loop through all quakes
    for quake in quakes:
        if quake['properties']['mag'] > largest['properties']['mag']:
            largest = quake

    print(largest['properties']['mag']) 

    # get coordinates of this
    long = largest['geometry']['coordinates'][0]
    lat = largest['geometry']['coordinates'][1]

    print('Latitude: {}, Longitude: {}'.format(lat,long))
