# This program returns the current weather for a location within the US,
# first prompting the user to choose zip code or city and state lookup, then
# prompting for the location info before hitting a location lookup api. The
# latitude and longitude returned from the api, and the user is prompted for
# temperature units. The latitude, longitude, and units are fed into another
# api, which returns the weather data for that location. The api response is
# then fed into another function which returns a user-friendly print of the
# data. After receiving the weather data, the user is prompted to repeat the
# process or quit.

# The following packages must be imported for this program:
# requests to make api calls
# json to convert json responses to dictionaries
# sys to exit the program
import requests
import json
import sys

# The api requires a key be attached in the url in every instance, set as a
# global variable here for use in all 3 api call functions.
app_key = '78f94649f98ee43f3283351c7465716a'

# The function request_exceptions catches errors that may arise when making
# api calls. In the try, a basic get request is attempted, then it checks to
# ensure the return is a json object, and finally it checks for any HTTP
# response codes that would indicate a failure. The except statements will
# print out a statement to the user indicating the issue, then the program is
# ended with an exit code of 1.


def request_exceptions(url):
    try:
        requests.get(url)
        requests.get(url).json()
        requests.get(url).raise_for_status()
    except requests.URLRequired:
        print('There was an issue with the URL sent to the api.')
        sys.exit(1)
    except requests.ConnectionError:
        print('There was a connection error when contacting the api.')
        sys.exit(1)
    except requests.Timeout:
        print('The request to the api timed out.')
        sys.exit(1)
    except requests.HTTPError:
        print('There was an HTTP error (' +
              dict(json.loads(requests.get(url).text))['cod'] +
              ') when contacting the api.')
        if dict(json.loads(requests.get(url).text))['cod'] == '404':
            print('Please check your inputs and try again.')
        sys.exit(1)
    except requests.TooManyRedirects:
        print('There were too many redirects.')
        sys.exit(1)
    except json.decoder.JSONDecodeError:
        print('There was an issue decoding the response text to JSON.'
              '\nPlease check your inputs and try again.')
        sys.exit(1)
    except requests.RequestException:
        print('An unknown error has occurred when contacting the api.')
        sys.exit(1)
    else:
        print('Connection to the API was successful.')


# The function request_exceptions_city_state catches errors that may arise
# when making api calls. In the try, a basic get request is attempted, then
# it checks to ensure the return is a json object, and finally it checks for
# any HTTP response codes that would indicate a failure. The except
# statements will print out a statement to the user indicating the issue,
# then the program is ended with an exit code of 1. This function is very
# similar to request_exceptions, but it is only used for the location api
# call based around city and state, as the return needs to be adjusted before
# checking if the response is a json object (The first and last character in
# the string need to be removed before converting to json).


def request_exceptions_city_state(url):
    try:
        requests.get(url)
        json.loads(requests.get(url).text[1:-1])
        requests.get(url).raise_for_status()
    except requests.URLRequired:
        print('There was an issue with the URL sent to the api.')
        sys.exit(1)
    except requests.ConnectionError:
        print('There was a connection error when contacting the api.')
        sys.exit(1)
    except requests.Timeout:
        print('The request to the api timed out.')
        sys.exit(1)
    except requests.HTTPError:
        print('There was an HTTP error (' +
              dict(json.loads(requests.get(url).text))['cod'] +
              ') when contacting the api.')
        if dict(json.loads(requests.get(url).text))['cod'] == '404':
            print('Please check your inputs and try again.')
        sys.exit(1)
    except requests.TooManyRedirects:
        print('There were too many redirects.')
        sys.exit(1)
    except json.decoder.JSONDecodeError:
        print('There was an issue decoding the response text to JSON.'
              '\nPlease check your inputs and try again.')
        sys.exit(1)
    except requests.RequestException:
        print('An unknown error has occurred when contacting the api.')
        sys.exit(1)
    else:
        print('Connection to the API was successful.')


# The function zip_lookup prompts the user for the zip code of the location
# that they would like to get the weather for. It does some basic validation
# of the zip code before passing it into the request_exceptions function. It
# first makes sure the zip code is an integer, then makes sure the zip code
# has a length of 5. Then zip code is inserted into the relevant url before
# running a get request. The response text is then converted to a dictionary
# and returned as an output.


def zip_lookup():
    zip_code = input('\nPlease enter your zip code:\n')
    try:
        int(zip_code)
    except ValueError:
        print('Please enter zip code as a 5 digit number')
        sys.exit(1)
    else:
        pass
    if len(zip_code) != 5:
        print('Please enter zip code as a 5 digit number')
        sys.exit(1)
    zip_url = ('http://api.openweathermap.org/geo/1.0/zip?zip=' + zip_code +
               ',US&appid=' + app_key)
    request_exceptions(zip_url)
    zip_json = requests.get(zip_url)
    zip_dict = json.loads(zip_json.text)
    return zip_dict


# The function city_state_lookup prompts the user for the city and state of
# the location that they would like to get the weather for. It does some
# basic validation of the state before passing it into the
# request_exceptions_city_state function. It makes sure the state is an
# abbreviation for one of the 50 states, or DC. Then city and state are
# inserted into the relevant url before running a get request. The response
# text is then converted to a dictionary and returned as an output. This
# function is very similar to the zip_lookup function, but the url is
# adjusted to handle city and state rather than zip. In addition, the output
# from the request needs to be manipulated slightly differently from the zip
# code return to get the dictionary return. The json object must have the
# first and last object removed to convert to a dictionary.


def city_state_lookup():
    city = input('\nPlease enter your city:\n')
    state = input('Please enter your 2 digit state code:\n')
    if state.upper() in ('AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC',
                         'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN',
                         'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN',
                         'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ',
                         'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI',
                         'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA',
                         'WI', 'WV', 'WY'):
        pass
    else:
        print('Please enter a valid US state abbreviation.')
        sys.exit(1)
    city_state_url = ('http://api.openweathermap.org/geo/1.0/direct?q=' +
                      city + ',' + state + ',US&appid=' + app_key)
    request_exceptions_city_state(city_state_url)
    city_state_json = requests.get(city_state_url)
    city_state_dict = json.loads(city_state_json.text[1:-1])
    return city_state_dict


# The function weather requires inputs of a dictionary containing a latitude
# and a longitude, as well as the units that the weather will be returned in.
# The lat and lon come from the location lookup api. In the main function,
# the user is prompted for the units they would prefer, then the units are
# converted to the correct input that the url requires. The
# request_exceptions function is called again to catch an errors that may
# arise from the call to the api. Once again, the response is converted to a
# dictionary and returned as an output.


def weather(lat_lon_dict, units):
    weather_url = ('https://api.openweathermap.org/data/2.5/weather?lat=' +
                   str(lat_lon_dict['lat']) + '&lon=' +
                   str(lat_lon_dict['lon']) +
                   '&exclude=minutely,hourly,daily,alerts&appid=' + app_key +
                   '&units=' + units)
    request_exceptions(weather_url)
    weather_json = requests.get(weather_url)
    weather_dict = json.loads(weather_json.text)
    return weather_dict


# The function compass_heading takes a degree heading and converts it to a
# compass heading for ease of reading. Each compass heading covers a 45
# degree range (North ranges from 337.5 to 22.5 degrees).


def compass_heading(degrees):
    if degrees > 337.5:
        heading = 'North'
    elif degrees > 292.5:
        heading = 'Northwest'
    elif degrees > 247.5:
        heading = 'West'
    elif degrees > 202.5:
        heading = 'Southwest'
    elif degrees > 157.5:
        heading = 'South'
    elif degrees > 112.5:
        heading = 'Southeast'
    elif degrees > 67.5:
        heading = 'East'
    elif degrees > 22.5:
        heading = 'Northeast'
    else:
        heading = 'North'
    return heading


# The function pretty_print takes 3 inputs: the output from the weather
# function, the temperature units requested by the user, and the units of
# wind speed and prints it into a readable format for the user. Variables are
# created for all the desired outputs from the weather api. The temperature
# is set to be displayed to 2 decimal points. There are 3 outputs that are
# not always returned from the api: wind gust speed, snowfall in the last
# hour, and rainfall in the last hour. To check whether these outputs are
# present before attempting to print them, try-except statements are used to
# skip calling the lines if the output was not returned and would cause an
# error to call and print.


def pretty_print(forecast_dict, temperature_units, wind_speed_units):
    city = forecast_dict['name']
    current = dict(forecast_dict['main'])['temp']
    feels_like = dict(forecast_dict['main'])['feels_like']
    high = dict(forecast_dict['main'])['temp_max']
    low = dict(forecast_dict['main'])['temp_min']
    pressure = dict(forecast_dict['main'])['pressure']
    humidity = dict(forecast_dict['main'])['humidity']
    wind_speed = dict(forecast_dict['wind'])['speed']
    wind_direction = dict(forecast_dict['wind'])['deg']
    wind_compass = compass_heading(wind_direction)
    cloud_coverage = dict(forecast_dict['clouds'])['all']
    print('\nCurrent weather in', city + ':'
          '\nIt is', "{:,.2f}".format(current), temperature_units,
          'outside, but it feels like', "{:,.2f}".format(feels_like),
          temperature_units,
          '\nThe high and low in the area are', "{:,.2f}".format(high),
          temperature_units, 'and', "{:,.2f}".format(low), temperature_units,
          '\nThe wind is going', wind_compass, '(' + str(wind_direction) +
          '°) at', wind_speed, wind_speed_units,
          '\nThere is', cloud_coverage, 'percent cloud coverage',
          '\nThe atmospheric pressure is', pressure, 'hPa',
          '\nThe humidity is', humidity/100)
    try:
        wind_gust = dict(forecast_dict['wind'])['gust']
    except KeyError:
        pass
    else:
        print('Expect gusts of wind up to', wind_gust, wind_speed_units)
    try:
        rain = dict(forecast_dict['rain'])['1h']
    except KeyError:
        pass
    else:
        print('There have been', rain, 'mm of rain in the last hour')
    try:
        snow = dict(forecast_dict['snow'])['1h']
    except KeyError:
        pass
    else:
        print('There have been', snow, 'mm of snow in the last hour')


# The main function is a loop that keeps the program running until the user
# chooses not to make another request. First a welcome message is printed to
# the user, then the user is asked how they would like to enter their
# location, via zip or city and state. If the user provides an incompatible
# input, the function will quit with an exit code of 1. The location api is
# called for either zip or city and state based on the user input. After a
# successful return from the location api, the user is asked to input which
# units they would like temperature provided in. Once again, there is
# validation around this input to quit with an exit code of 1 on a bad input.
# Upon the successful return of the current weather data, the print command
# is called to output the data to the user in a readable format. Finally, the
# user is prompted to either repeat the process or quit.


def main():
    loop_command = 'y'
    print('Welcome, we provide current weather data for any location within '
          'the US, using either a ZIP code or city and state.')
    while loop_command == 'y':
        city_or_zip = input('Which would you like the forecast for:'
                            '\n1) zip code'
                            '\n2) city and state\n')
        if city_or_zip == '1':
            loc_api_response = zip_lookup()
        elif city_or_zip == '2':
            loc_api_response = city_state_lookup()
        else:
            print('Please enter only \"1\" or \"2\".')
            sys.exit(1)
        temp_units = input('\nWhat units would you like your temperature in:'
                           '\n1) Fahrenheit'
                           '\n2) Celsius'
                           '\n3) Kelvin\n')
        if temp_units == '1':
            weather_dict = weather(loc_api_response, 'imperial')
            temp_units = '°F'
            wind_units = 'mph'
        elif temp_units == '2':
            weather_dict = weather(loc_api_response, 'metric')
            temp_units = '°C'
            wind_units = 'm/s'
        elif temp_units == '3':
            weather_dict = weather(loc_api_response, 'standard')
            temp_units = 'K'
            wind_units = 'm/s'
        else:
            print('Please enter only \"1\", \"2\", or \"3\".')
            sys.exit(1)
        pretty_print(weather_dict, temp_units, wind_units)
        loop_command = input('\nPress \"y\" if you would like to run again:'
                             '\n')
        if loop_command == 'y':
            print('\n')
        elif loop_command == 'Y':
            loop_command = 'y'
            print('\n')
        else:
            print('Shutting down process. Thank you')


main()
