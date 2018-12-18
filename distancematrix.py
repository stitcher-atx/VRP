"""
Okay so this code might be cruddy as all get out but it works for me, like multiple times. I had to run the apidistance() inside
of the buildmatrix() so that it would run asynchronously in python. I could add a queue to thread this shit but that seemed like more
work than neccessary at this time.
"""



import requests
import pandas as pd
import itertools

#file needs to be already run through the geocode.py so that 'Latitude' and 'Longtidue' are valiable column names
file = "invoices.csv"
apikey = "YOUR_API_KEY"

def apidistance():
    df = pd.read_csv(file, header= 0)
    df = pd.DataFrame(df)
    df['xy'] = df.apply(lambda x: [x['Latitude'], x['Longitude']], axis=1).astype(str)
    df['xy'] = df['xy'].str.strip('[]')
    # |pipes separate destinations
    cord = "|".join(df['xy'])
    cord = cord.replace(" ","")
    url = ("https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + cord
           + "&destinations="+ cord + "&mode=driving&language=en-EN&key=" + apikey)
    return url

def buildmatrix(url):
    #Take google api response json and make it parseable for python
    resp = requests.get(url=url)
    data = resp.json()

    #A dictionary to store lists of distances from any spot
    dictdf = {}

    #Needed to make the while loop over all elements for each row, probably not pythonic but it f* it
    i = 0
    destinations = (len(data['destination_addresses']))

    #Parse the json
    while i < destinations:
        #variable to store distances from a spot
        distances =[]
        #structure of list to be updated to dictionary
        fromstop =[i,distances]
        for rows in data['rows'][i]['elements']:
                distances.append(rows['distance']['value']*0.000621) #,rows['duration']['value']]) other things found in the json
        #updating dictionary of distances
        d = dict(itertools.zip_longest(*[iter(fromstop)] * 2, fillvalue=""))
        dictdf.update(d)
        #move to next element to loop over
        i += 1

    #convert fictionary into a matrix, hell yeah!
    df = pd.DataFrame.from_dict(dictdf, orient='index')
    print (df)

def main():
    buildmatrix(apidistance())

if __name__ == '__main__':
    main()
