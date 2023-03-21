# JavaScript Object Notation
# JSON represents data as nested "lists" and "dictionaries"
# Similar to dict()

import json
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
}
'''

# Parses string and returns a python dictionary
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
