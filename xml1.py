import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
#    api_key = 42
#    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
#else :
    #serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
file=input('enter: ')
xml = urllib.request.urlopen(file, context=ctx).read()
tree=ET.fromstring(xml)
lst=tree.findall('comments/comment')
sum=0
for item in lst:
    x=item.find('count').text
    x=int(x)
    sum=sum+x
print(sum)
