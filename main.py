import requests
import json
import time
from dotenv import get_key, load_dotenv
import os
load_dotenv()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

if __name__ == "__main__":

    # Define the API key, define the endpoint, and define the header
    api_key = os.environ['SECRET_KEY']
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'bearer %s' %api_key}

    # Define the parameters
    parameters = {'term': 'ramen',
                'limit': '50',
                'radius': 10000,
                'location': 'San Francisco'}

    # Make a request to the Yelp API
    response = requests.get(url= endpoint, params= parameters, headers= headers)
    #jprint(response.json())

    # Convert JSON string to dict
    business_data = response.json()

    # Stores name, id of businesses in dict if there is a value for price
    dict = {}
    for biz in business_data['businesses']:
        if 'price' not in biz:
            continue
        else:
            dict[biz['name']] = biz['id']

    # Main setup
    print('Hi there! Shortly, we will provide with you a list of businesses offering ramen in San Francisco.')
    print('If you want information on a particular business, you will be asked to input the name of that business.')
    print('Then, information about the business will be provided to you.')
    print('You can choose as many business as you like. If you want to quit, you will be prompted to input "q".')
    time.sleep(10)
    print('Here are the businesses our search resulted in:')
    print()
    time.sleep(5)

    # Prints list of businesses
    for key in dict.keys():
        print(key)
    
    # Finds information about a particular business for the user
    print()
    user_input = ''
    while user_input != 'q':
        # Checks if key was entered correctly
        biz_name = input('Type the name of the business that you are interested in.\n')
        valid = True
        while valid == True:
            if biz_name not in dict.keys():
                print('Oops! You may have entered the wrong business name. Please try again.\n')
                biz_name = input()
            else:
                valid = False
    
        # Gathers data about specific restaurant by adding id to endpoint
        biz_id = dict[biz_name]
        id_endpoint = "https://api.yelp.com/v3/businesses/" + biz_id
        response = requests.get(url= id_endpoint, params= parameters, headers= headers)
        restaurant_data = response.json()
        #jprint(restaurant_data)
        
        # Stores information about business
        price = restaurant_data['price']
        rating = restaurant_data['rating']
        location = " ".join(restaurant_data['location']['display_address'])
        categories = restaurant_data['categories'][0]['title']
        reviews = restaurant_data['review_count']

        # Prints information to users
        print()
        print(f"{biz_name}'s category is listed as '{categories}.'")
        print(f"They are located at {location}.")
        print(f"Their rating is {rating}, based on a total of {reviews} reviews.")
        print(f"Their price range is {price}.")

        # Asks users whether they want to continue
        user_input = input("Would you like to continue? Press 'q' for quit, and any other key to continue.\n")

        
        


