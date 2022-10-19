# yelp_api_project
This project parses through data from the YelpAPI to find information about restaurants serving ramen in San Francisco, CA.

# Purpose
The purpose of this project was mainly for practicing skills associated with parsing data from an API. These skills include using get requests, creating environment variables to hide sensitive information (e.g. API key), authorizing access to the data, filtering results based on specific parameters, and looping through dictionaries to find particular values.

# Overview
This program creates a dictionary based on businesses in San Francisco, CA that serve ramen. The user is presented with the names of businesses, chooses one, and receives information about the business, such its price, rating, and location. The user can repeat the process to see information about other businesses. 

# Project Usage
The user will need to create a Yelp account to successfully run the code. Once an account is created, they will have to create an app so that they can get their unique API key. This project stored the API key in an .env file so that it could be used locally without raising security issues when the file was uploaded to GitHub.

