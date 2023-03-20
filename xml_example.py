# eXtensible Markup Language
# Purpose: To help information systems share structered data

# Tags: Indicates the beginning and ending of elements
# Attributes: Keyword/value pairs on the opening tag of XML
# Serialize/De-serialize: Convert data in one program into 
# a common format that can be stored and/or transmitted between
# systems in a programming language-independant manner

# e.g.
# <person> # Start Tag (<person>)
#   <name>Chuck</name> # End Tag (</name>)
#   <phone type='intl'> # Attribute (type = 'intl')
#   +1 734 303 4456 # Text Content (ph number)
#   </phone>
#   <email hide="yes"/> # Self Closing Tag (<email />)
# </person>

# White space is not too important 
# (but is important for ph number above)

# We can validate an XMl document if we have 
# an XML contract to check against (XSD is popular XML structure)

# Example 1
import xml.etree.ElementTree as ET
data = '''
<person>
  <name>Chuck</name>
  <phone type='intl'>
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) # ("Chuck")Pulls the text from within tag <name>
print('Attr:', tree.find('email').get('hide')) # ("yes") Get attribute of <email>

# Example 2
import xsml.etree.ElementTree as ET
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))
for item in lst:
  print('Name', item.find('name').text)
  print('Id', item.find('id').text)
  print('Attribute', item.get("x"))
