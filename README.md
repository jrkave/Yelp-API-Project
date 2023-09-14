# Yelp API Project
## Description
The Yelp API Project is a Python script that integrates with the Yelp Fusion API to fetch details about various restaurants serving ramen in San Francisco, California, using predefined criteria to filter results. After the list of businesses is provided, the user will be able to input the names of businesses they're interested in, at which point more information (specific to that business) will be output. 

## Table of Contents
- Features
- Code Overview
- Usage

## Features
1. **Yelp Fusion API Integration**: leverages the Yelp Fusion API to fetch detailed information about various businesses
2. **Environment Variables**: creates environment variables to hide sensitive information (e.g. API key)
3. **Authorization**: ensures that only users with a unique API key will be able to use the program

## Code Overview
The program creates a dictionary based on businesses in San Francisco, CA that serve ramen. The user is presented with the names of businesses, chooses one, and receives information about the business, such its price, rating, and location. The user can repeat the process to see information about other businesses. 

## Usage
The user will need to create a Yelp account to successfully run the code. Once an account is created, they will have to create an app so that they can get their unique API key. This project stores an API key in an .env file so that it can be used locally without raising security issues.
To clone the repository, run this command: `git clone https://github.com/jrkave/Yelp-API-Project.git`

