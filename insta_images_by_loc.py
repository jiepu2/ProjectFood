import requests
import json
from geoloc import coordinates

client_id="fcea843200a7447b967cc616e9efa79d"                              #client ID
client_secret="eba26794ddee490687e35cdb172357d5"                          #client Secret
redirect_uri="http://localhost"                                           #redirect uri
grant_type="authorization_code"                                           #default option provided by Instagram

def get_access_token():
    access_token="715368389.0912694.a9b928f66e5e4ed5997b9012e4ddc602"
    return access_token

def media_search(lat,lng,access_token):
    max_timestamp = 1504746309
    for j in range(20):
        url="https://api.instagram.com/v1/media/search?lat="+lat+"&lng="+lng+"&distance=5000"+"&access_token="+access_token + "&max_timestamp="+str(max_timestamp)
        r=requests.get(url)
        resp=json.loads(r.text)
        num = 20
        for i in range(num):
            pic_url=resp['data'][i]['images']['standard_resolution']['url']         #getting the image url
            p=requests.get(pic_url)
            f_name=str(location)+ ' pic ' + str(i+j*20) + '.jpg'
            with open(f_name,'wb') as f:
                f.write(p.content)
                f.close()
            print("Image No." + str(i+j*20) + " Downloaded")
            max_timestamp = int(resp['data'][i]['created_time'])-1

location=input("Please enter the city name.\n")
c=coordinates(location)
lat=str(c[0])
lng=str(c[1])

access_token=get_access_token()
media_search(lat, lng, access_token)
