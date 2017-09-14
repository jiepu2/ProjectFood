import requests
import json
import csv

client_id="fcea843200a7447b967cc616e9efa79d"                              #client ID
client_secret="eba26794ddee490687e35cdb172357d5"                          #client Secret
redirect_uri="http://localhost"                                           #redirect uri
grant_type="authorization_code"                                           #default option provided by Instagram

def get_access_token():
    access_token="715368389.0912694.a9b928f66e5e4ed5997b9012e4ddc602"
    return access_token

def get_coordinates(locations):
    search = []
    for row in locations:
        if len(row):
            coordinate = []
            coordinate.append(row[0])
            coordinate.append(row[1])
            search.append(coordinate)
    return search

def media_search(lat,lng,access_token,title):
    max_timestamp = 1504746360
    for j in range(1):
        url="https://api.instagram.com/v1/media/search?lat="+lat+"&lng="+lng+"&distance=5000"+"&access_token="+access_token + "&max_timestamp="+str(max_timestamp)
        r=requests.get(url)
        resp=json.loads(r.text)
        num = 20
        timestamps=[]
        for i in range(len(resp['data'])):
            pic_url=resp['data'][i]['images']['standard_resolution']['url']         #getting the image url
            p=requests.get(pic_url)
            f_name=resp['data'][i]['id'] + '.jpg'
            with open(f_name,'wb') as f:
                f.write(p.content)
                f.close()
            print("Image No." + str(i+j*20) + " Downloaded")
            timestamps.append(int(resp['data'][i]['created_time']))
        max_timestamp = min(timestamps)-60


locations =  "./Coordinates.csv"

with open(locations, 'rt') as file:
    reader = csv.reader(file)
    locations = list(reader)

coordinates = get_coordinates(locations)
access_token=get_access_token()

i = 0
for item in coordinates:
    lat=str(item[1])
    lng=str(item[0])
    i += 1
    media_search(lat, lng, access_token, i)


