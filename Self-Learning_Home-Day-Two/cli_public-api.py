import requests
import json
import urllib2

# This short program is a simple command line python application that takes the name of a country and prints out the  information about countries via a RESTful API
# It uses a RESTful API from https://restcountries.eu/     REST Countries


headers = {'Content-type': 'application/json'}
# this takes a python object and dumps it to a string which is a JSON
# representation of that object

def get_country_data(country):
    # open the url and the screen name
    # (The screen name is the screen name of the user for whom to return results for)
    url = 'https://restcountries.eu/rest/v1/name/' + country
    r = requests.get(url)
    country_info = r.json()

    return country_info

while True:
    desired_country = str(raw_input('Please enter a country name and I will give you the data for that country.\nPress enter without any text to exit: ').lower())
    if desired_country == '':
        break

    else:
        country_data = get_country_data(desired_country)
        # Print the status code of the response.
        #print(response.status_code)

        if country_data[0]['name'].lower() == desired_country.lower():
            print ('\nThe country name is ' + country_data[0]['name'] )
            print ('Capital City: ' + str(country_data[0]['capital']))
            print ('Population: ' + str(country_data[0]['population']))
            print ('Its in Region: ' + str(country_data[0]['region']))
            print ('In Subregion: ' + str(country_data[0]['subregion']))
            print ('It Borders: ' + str(country_data[0]['borders']))
            print ('The languages spoken are: ' + str(country_data[0]['languages']))
            print ('The Currencies in use are: ' + str(country_data[0]['currencies']))
            print ('The CallingCodes=: ' + str(country_data[0]['callingCodes']))
            print ('The Top Level Domain is: ' + str(country_data[0]['topLevelDomain']))
            print ('The Alpha Code is: ' + str(country_data[0]['alpha2Code']))

        else:
            print("Sorry. I couldn't get information for that country.\n")
