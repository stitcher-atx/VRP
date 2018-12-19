"""
I am using geopy to geocode locations into lat/long pairs. Yeah, I could use Google Api for this as well, but I am trying to spread out costs. Geocode is free so we are using it. I have noticed taking geopy cords and feeding them to Google Distance Api might return slightly off responses from Google. But, the response is off by like 5 yards. Good enough for vehicle routing, but maybe not cruise missiles, or killer drones. Neither of those things I condone with the use of my code. However, geopy.geocoders request you put your name, organization, and/or app name so they can see who is generating traffic to their service. Please change "user_agent" to reflect who/what you are doing by using their services, you freeloader. Also, make sure you have your "invoices.csv" has a column named "Location" and it is in the same dir. 
"""

from geopy.geocoders import Nominatim
import pandas as pd

file = "invoices.csv"
user_agent= "Who_are_you" 

#Call geopy api to get an alternative name, lat, and long for a given entry
def latlong():
    nom = Nominatim(user_agent=user_agent)
    df = pd.read_csv(file)
    df["GeoCodeName"] = df["Location"].apply(nom.geocode)
    df["Latitude"] = df["GeoCodeName"].apply(lambda x: x.latitude if x != None else None)
    df["Longitude"] = df["GeoCodeName"].apply(lambda x: x.longitude if x != None else None)
    #considering storing to a variable insteaf of to a file. another challenge for another day
    df.to_csv(file)

    

#this returns a list required by main app function create_data_model(): ... looks like im using the Google's OR-tools
def cord():
    _locations = []
    colnames = [ 'name', 'latitude', 'longitude']
    df = pd.read_csv(file, names=colnames, header=0)
    stopsname = df.name.tolist()
    lat = df.latitude.tolist()
    long = df.longitude.tolist()
    cord = list(zip(lat,long))
    stops = list(zip (stopsname,cord))
    for stopcords in (i[1] for i in stops):
        _locations.append(stopcords)
    return _locations
    #print(_locations)
    
def main():
   latlong()

if __name__ == '__main__':
    main()

