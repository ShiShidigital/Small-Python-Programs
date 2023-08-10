# Programm to get the Longitude and Latitude from a Country or a City
print()
print('--- Get Longitude and Latitude of a Place with this App! ---')

#Import stuff 
import urllib.request, urllib.parse, urllib.error
import ssl 
import json


# Functions
def get_data_from_url(url):
    js_data = None 
    
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print('Connecting to URL:', url)
    # Get data from URL
    try:
        raw_data = urllib.request.urlopen(url, context=ctx).read()
        data = raw_data.decode()
    except:
        print('Did not get data from URL.')
        data = None
    # print(data)

    # turn json data into dictionary
    try:
        js_data = json.loads(data)
    except:
        print('Could not translate data into dictionary')
        js_data = None

    return js_data


def get_lon_lat_from_place():
    while True:
    # Get input from User (Placename as String)
        print('\nPlease enter the Placename below:')
        user_input = input(' > ')

        # Do some sanity checking of the user input
        if len(user_input) > 1:
            placename = user_input.lower()
            # print(placename)
        else:
            print('Invalid Input! Try again!')
            continue

        print('Building URL ...') 
        url = ('https://geocoding-api.open-meteo.com/v1/search?' + 
               '{}&count=10&language=en&format=json'.format(
                   urllib.parse.urlencode({'name':placename})))
        # print(url)

        js_data = get_data_from_url(url)
        print()
 
        # Check via Geocoding API if that Place exists
        if js_data == None:
            print('Could not get any data.')
            continue

        if "results" not in js_data:
            print('Place does not exist.')
            continue
         
        # if there are more places with that name
        # let user choose from list
        places = js_data['results']
        citylist = []
        count = 0

        for place in places:    # Limit Places via Population amount
            if 'population' in place:
                # print(place['name'], place['country'], place['population'])
                count += 1

                if place['population'] >= 10000:
                    citylist.append(place)
                    # print('-> Has more than 10000 population')
                
                elif place['population'] >= 1000:
                    if len(citylist) >= 5:
                        continue   
                    citylist.append(place)
                    # print('-> Has more than 1000 population')

                elif place['population'] >= 100:
                    if len(citylist) >= 1:
                        continue 
                    citylist.append(place)
                    # print('-> Has more than 100 population')

                else:
                    continue
                    # print('-> Has less than 100 population')
                    

        # print('There are ', count, 'places named like this.') 
        # print('Citylist len:', len(citylist))

        c_count = 0
        for city in citylist:
            c_count += 1
            exact_place = (city['name'] + ', Population: ' + str(city['population']) 
                        + ',\n Location: ' + city['country'] )
            # print(city['name'], city['population'], city['country'])  
            if 'admin1' in city: exact_place = exact_place + ', ' + city['admin1']
            if 'admin2' in city: exact_place = exact_place + ', ' + city['admin2']
            if 'admin3' in city: exact_place = exact_place + ', ' + city['admin3']
            if 'admin4' in city: exact_place = exact_place + ', ' + city['admin4']

            print(str(c_count) + ') ' + exact_place)

        user_input = input('Choose city from citylist > ')
        try:
            ch_city = int(user_input) - 1

            if ch_city > len(citylist) or ch_city < 0: 
                print('Choose a number from the list')
                continue
        except:
            print('Please enter a number...')
            continue
        
        print()
        # print('Choosen City:', citylist[ch_city])

        print('- Choosen city data:')
        # Return Longitude and Latitude 
        cityname = citylist[ch_city]['name']
        country = citylist[ch_city]['country']
        print(cityname, '-', country)
        lat = citylist[ch_city]['latitude']
        lon = citylist[ch_city]['longitude']
        print('Lat:', lat, 'Lon:', lon)

        return lon, lat


# While Loop Menu
while True:
    print('\nMENU')
    print('0) Exit App')
    print('1) Find Longitude and Latitude from a place')

    print('Choose from Menu > ')
    user_input = input()

    try:
        menu_choice = int(user_input)
    except:
        print('Please enter a number...')
        continue


    if menu_choice == 0:
        print('Tschüss!')
        quit()


    elif menu_choice == 1:
        lon_lat = get_lon_lat_from_place()
        print(lon_lat)


    else:
        print('Not a good choice!')
        continue 
