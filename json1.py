import urllib.request,urllib.parse,urllib.error
import json
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
file=input('enter: ')
js = urllib.request.urlopen(file, context=ctx).read()
data=json.loads(js)   #returns a dictionary
#lst=tree.findall('comments/comment')
sum=0
lst=data['comments']
for item in lst:
    #x=item.find('count').text
    x=item['count']
    x=int(x)
    sum=sum+x
print(sum)
