import urllib.request, urllib.parse, urllib.error
import ssl 
import json


print()
print("--- Mastodon Public Timeline Reader ---")

# Defaults
limit = 5  # Define limit of posts you want to get from timeline
server = 'troet.cafe'   


while True:
    print("\nMENU")
    print("0) Exit Program")
    print("1) Show {} posts from public timeline from {}".format(limit, server))
    print("2) Change Server")
    print("3) Change amount of posts you want to receive")

    user_input = input("Please choose a Menu Option >> ")

    try:
        user_choice = int(user_input)
    except:
        print("Only numbers, please!")
        continue 


    if user_choice == 0:
        print('Good Bye!')
        exit()

    elif user_choice == 1:
        #Get Public Timeline from server
        print()
        print('* Calling on Mastodon...')
        url = 'https://{}/api/v1/timelines/public?limit={}'.format(server, limit)
        print('Using URL:', url)

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        # Connect and read data
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        # print(type(data), data[:50])  #string
        print('Received', len(data), 'Characters.')

        # Change data to json
        js = json.loads(data) 
        # print(type(js))   # list
        print('Received', len(js), 'list entrys.\n')

        for item in js:
            print()
            # print(item)   # Dictionary
            print('Created:', item['created_at'])
            print('From Account:', item['account']['display_name'])
            print('Bot? ', item['account']['bot'])
            print('Message: ', item['content'])
        
        connection.close()

    elif user_choice == 2:
        print('Find a list of Mastodon Servers here: https://joinmastodon.org/servers')
        user_input = input('Please type in a server name >> ')
        server = user_input

    elif user_choice == 3:
        print('Be aware that a huge number of posts take some time to load.')
        limit = int(input('Please give the number of posts you want to receive > '))

    else:
        print('Please choose a valid MENU option: 0, 1, 2, 3')
        continue

    





