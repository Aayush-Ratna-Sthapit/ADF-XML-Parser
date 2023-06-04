import re

l = 'lead1.xml'
jfile = re.sub(".xml", "", l) + '.json'
print(jfile)
