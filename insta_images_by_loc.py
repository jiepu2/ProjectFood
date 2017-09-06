import requests
import json
from geoloc import coordinates

client_id="fcea843200a7447b967cc616e9efa79d"                              #client ID
client_secret="eba26794ddee490687e35cdb172357d5"                          #client Secret
redirect_uri="http://localhost"                                           #redirect uri
grant_type="authorization_code"                                           #default option provided by Instagram

def get_access_token():
    access_token="715368389.e029fea.2c76ea92adff40db8258679d1064d7ab"
    return access_token

def media_search(lat,lng,access_token):
    url="https://api.instagram.com/v1/media/search?lat="+lat+"&lng="+lng+"&distance=5000"+"&access_token="+access_token
    r=requests.get(url)
    resp=json.loads(r.text)
    num = 20
    for i in range(num):
        pic_url=resp['data'][i]['images']['standard_resolution']['url']         #getting the image url
        p=requests.get(pic_url)
        f_name=str(location)+ ' pic '+str(i)+'.jpg'
        with open(f_name,'wb') as f:
            f.write(p.content)
            f.close()
        print("Image No." + str(i) + " Downloaded")

location=input("Please enter the city name.\n")
c=coordinates(location)
lat=str(c[0])
lng=str(c[1])

access_token=get_access_token()
media_search(lat, lng, access_token)
