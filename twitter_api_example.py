import urllib.request, urllib.parse, urllib.error
import twurl
import json

# API name - base url we are going to use for the API
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
  print('')
  acct = input('Enter twitter account: ')
  if len(acct) < 1: break
  # Get the first 5 friends of this screen name
  # twurl includes all api account info
  url = twurl.augment(TWITTER_URL,
                      {'screen_name': acct, 'count': '5'})
  print('Retrieving', url)
  # Open url connectioned and receive data from api
  connection = urllib.request.urlopen(url)
  # Read the data and decode from bytes to string
  data = connection.read().decode()
  # Extract header from the recieved data into a dict to inspect
  headers = dict(connection.getheaders())
  # See the remaining number of api calls from header dicitonary
  print('Remaining', headers['x-rate-limit-remaining'])
  # Convert the data from string to json format
  js = json.loads(data)
  # Print the json file with indentation 'pretty indenting'
  print(json.dumps(js, indent=4))
  
  for u in js['users']:
    print(u['screen_name'])
    s = u['status']['text']
    # Adding 4 spaces to text for pretty indenting
    print('   ', s[:50])
