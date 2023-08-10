import urllib.request, urllib.parse, urllib.error
import ssl 
import bs4 as BeautifulSoup
import json


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
        print('Could not tranlate data into dictionary')
        js_data = None

    return js_data

def get_lon_lat_from_place():
    print('Finding out Longitude and Latitude of choosen place ...')
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
        
        # print('Choosen City:', citylist[ch_city])

        #print('- Choosen city data:')
        # Return Longitude and Latitude 
        cityname = citylist[ch_city]['name']
        country = citylist[ch_city]['country']
        # print(cityname, '-', country)
        lat = citylist[ch_city]['latitude']
        lon = citylist[ch_city]['longitude']
        # print('Lat:', lat, 'Lon:', lon)

        place_data = [cityname, lon, lat]

        return place_data



print('--- My Weather App ---')

while True:
    print('\nMENÜ')
    print('0) Exit App')
    print('1) Show todays Weather at a choosen place.')
    print('2) Show weather forecast for the next 3 days for a choosen place.')

    user_input = input('\nChoose a Menu Point > ')

    try:
        menu_choice = int(user_input)
    except:
        print('Choose a Menu point > ')
        continue


    if menu_choice == 0:
        print('Good Bye!')
        quit()
    
    elif menu_choice == 1:
        print('Get Weather data from a choosen place.')
        name_lon_lat = get_lon_lat_from_place()
        print('\nGetting Weather Data from following place:', name_lon_lat)

        url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max,windspeed_10m_max&current_weather=true&timezone=Europe%2FBerlin&models=best_match'.format(name_lon_lat[2], name_lon_lat[1])
        js = get_data_from_url(url)

        if js == None:
            print('No data here')
            continue

        print()
        print('Date:', js['daily']['time'][0])
        print('Current Temperature in {}:'.format(name_lon_lat[0]), js['current_weather']['temperature'], js['daily_units']['temperature_2m_max'])
        print('Max. Temperature today:', js['daily']['temperature_2m_max'][0], js['daily_units']['temperature_2m_max'])
        print('Min. Temperature today:', js['daily']['temperature_2m_min'][0], js['daily_units']['temperature_2m_max'])
        print('Chance for Rain:', js['daily']['precipitation_probability_max'][0], js['daily_units']['precipitation_probability_max'])
        print('Windspeed:', js['daily']['windspeed_10m_max'][0], js['daily_units']['windspeed_10m_max'])


    elif menu_choice == 2:
        print('Get Weather data from a choosen place.')
        name_lon_lat = get_lon_lat_from_place()
        print('\nGetting Weather Data from following place:', name_lon_lat)

        url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max,windspeed_10m_max&current_weather=true&timezone=Europe%2FBerlin&forecast_days=3&models=best_match'.format(name_lon_lat[2], name_lon_lat[1])
        js = get_data_from_url(url)

        if js == None:
            print('No data here')
            continue

        print()
        print('Date:', js['daily']['time'][0])
        print('Max. Temperature:', js['daily']['temperature_2m_max'][0], js['daily_units']['temperature_2m_max'])
        print('Min. Temperature:', js['daily']['temperature_2m_min'][0], js['daily_units']['temperature_2m_max'])
        print('Chance for Rain:', js['daily']['precipitation_probability_max'][0], js['daily_units']['precipitation_probability_max'])
        print('Windspeed:', js['daily']['windspeed_10m_max'][0], js['daily_units']['windspeed_10m_max'])

        print()
        print('Date:', js['daily']['time'][1])
        print('Max. Temperature:', js['daily']['temperature_2m_max'][1], js['daily_units']['temperature_2m_max'])
        print('Min. Temperature:', js['daily']['temperature_2m_min'][1], js['daily_units']['temperature_2m_max'])
        print('Chance for Rain:', js['daily']['precipitation_probability_max'][1], js['daily_units']['precipitation_probability_max'])
        print('Windspeed:', js['daily']['windspeed_10m_max'][1], js['daily_units']['windspeed_10m_max'])

        print()
        print('Date:', js['daily']['time'][2])
        print('Max. Temperature:', js['daily']['temperature_2m_max'][2], js['daily_units']['temperature_2m_max'])
        print('Min. Temperature:', js['daily']['temperature_2m_min'][2], js['daily_units']['temperature_2m_max'])
        print('Chance for Rain:', js['daily']['precipitation_probability_max'][2], js['daily_units']['precipitation_probability_max'])
        print('Windspeed:', js['daily']['windspeed_10m_max'][2], js['daily_units']['windspeed_10m_max'])


    else:
        print('Not a good choice! Repeat')
        continue 